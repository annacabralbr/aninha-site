// Visita o site antigo, descobre as páginas internas pelos links, salva prints
// (1440 e 390 px), o texto e o HTML renderizado em _ref/ e baixa as imagens do
// Framer para public/img/. Uso: node scripts/capturar.mjs
import { chromium } from "playwright"
import { mkdir, writeFile, access } from "node:fs/promises"

const BASE = "https://aninha.art.br"
const seen = new Set(["/"])
const queue = ["/"]
const images = new Map()
await mkdir("_ref", { recursive: true })
await mkdir("public/img", { recursive: true })

const browser = await chromium.launch()
const slug = (p) => (p === "/" ? "home" : p.replace(/^\//, "").replace(/\//g, "__"))

async function settle(page) {
    await page.waitForTimeout(1500)
    // rola até o fim para carregar imagens preguiçosas e disparar animações
    await page.evaluate(async () => {
        for (let y = 0; y < document.body.scrollHeight; y += 400) {
            window.scrollTo(0, y)
            await new Promise((r) => setTimeout(r, 150))
        }
        window.scrollTo(0, 0)
    })
    await page.waitForTimeout(1500)
}

while (queue.length && seen.size < 80) {
    const path = queue.shift()
    for (const [w, h, tag] of [
        [1440, 900, "d"],
        [390, 844, "m"],
    ]) {
        const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 })
        try {
            await page.goto(BASE + path, { waitUntil: "load", timeout: 60000 })
        } catch (e) {
            console.log("demorou para carregar, seguindo assim mesmo:", path)
        }
        await settle(page)
        await page.screenshot({ path: `_ref/${slug(path)}-${tag}.png`, fullPage: true })
        if (tag === "d") {
            await writeFile(`_ref/${slug(path)}.html`, await page.content())
            await writeFile(`_ref/${slug(path)}.txt`, await page.evaluate(() => document.body.innerText))
            const found = await page.evaluate(() => ({
                links: [...document.querySelectorAll("a[href]")].map((a) => new URL(a.getAttribute("href"), location.href)).filter((u) => u.origin === location.origin).map((u) => u.pathname),
                imgs: [...document.querySelectorAll("img")].map((i) => i.currentSrc || i.src).concat([...document.querySelectorAll("video")].flatMap((v) => [v.src, v.poster])).concat([...document.querySelectorAll("*")].map((e) => getComputedStyle(e).backgroundImage).filter((b) => b.includes("framerusercontent")).map((b) => b.slice(5, -2))),
            }))
            if (path === "/contato") {
                // formulário comercial: troca a aba e salva também
                try {
                    await page.getByText("COMERCIAL", { exact: true }).first().click()
                    await page.waitForTimeout(1500)
                    await page.screenshot({ path: "_ref/contato-comercial-d.png", fullPage: true })
                    await writeFile("_ref/contato-comercial.html", await page.content())
                } catch (e) {
                    console.log("sem aba comercial", e.message)
                }
            }
            for (const l of found.links) {
                const p = l.replace(/\/$/, "") || "/"
                if (!seen.has(p)) {
                    seen.add(p)
                    queue.push(p)
                }
            }
            for (const src of found.imgs) {
                const m = src.match(/framerusercontent\.com\/(images|assets)\/([A-Za-z0-9_-]+\.(png|jpe?g|webp|gif|svg|mp4))/)
                if (m) images.set(m[2], `https://framerusercontent.com/${m[1]}/${m[2]}`)
            }
        }
        await page.close()
    }
}
// arquivos usados em CSS (texturas) também vão
for (const f of ["fx4U97qkoGSIvuUQfvE8HZx3pa4.png"]) images.set(f, "https://framerusercontent.com/assets/" + f)
await browser.close()

for (const [name, url] of images) {
    const out = `public/img/${name}`
    try {
        await access(out)
        continue
    } catch {}
    const r = await fetch(url)
    if (r.ok) await writeFile(out, Buffer.from(await r.arrayBuffer()))
    else console.log("falhou", url, r.status)
}
await writeFile("_ref/paginas.txt", [...seen].join("\n") + "\n")
console.log("páginas:", [...seen].length, "imagens:", images.size)
