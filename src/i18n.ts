// Idiomas do site. Português é o principal (sem prefixo); inglês em /en e espanhol em /es.
export type Lang = "pt" | "en" | "es"
export const LANGS: Lang[] = ["pt", "en", "es"]
export const HTML_LANG: Record<Lang, string> = { pt: "pt-BR", en: "en", es: "es" }
export const base = (lang: Lang) => (lang === "pt" ? "" : `/${lang}`)
export const href = (lang: Lang, path: string) => (lang === "pt" ? path : path === "/" ? `/${lang}/` : `/${lang}${path}`)

// endereço da mesma página em outro idioma
export function switchTo(path: string, to: Lang) {
    const clean = path.replace(/^\/(en|es)(?=\/|$)/, "") || "/"
    return href(to, clean)
}

export const UI = {
    pt: {
        nav: ["Início", "Bio", "Discografia", "Mixes", "Agenda", "Contato"],
        navMain: "Principal",
        skip: "Pular para o conteúdo",
        home: "Aninha, página inicial",
        openMenu: "Abrir menu",
        closeMenu: "Fechar menu",
        footer: "Rodapé",
        footerAlt: "Retrato em preto e branco da Aninha",
        langs: "Idioma",
        siteTitle: "Aninha | DJ & Produtora de Música Eletrônica",
        labels: "Gravadoras",
        soon: "Novas datas em breve.",
        done: "Realizado",
        tickets: "Ingressos ↗",
        months: ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"],
        locale: "pt-BR",
        watch: "Assistir",
        alt: (a: string) => a,
    },
    en: {
        nav: ["Home", "Bio", "Discography", "Mixes", "Tour dates", "Contact"],
        navMain: "Main",
        skip: "Skip to content",
        home: "Aninha, home page",
        openMenu: "Open menu",
        closeMenu: "Close menu",
        footer: "Footer",
        footerAlt: "Black and white portrait of Aninha",
        langs: "Language",
        siteTitle: "Aninha | DJ & Electronic Music Producer",
        labels: "Record labels",
        soon: "New dates coming soon.",
        done: "Done",
        tickets: "Tickets ↗",
        months: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        locale: "en",
        watch: "Watch",
        alt: (a: string) =>
            a
                .replace(/^Capa de lançamento da Aninha$/, "Aninha release cover")
                .replace(/^Capa: /, "Cover: ")
                .replace(/^Cartaz dos 13 anos do Warung, 2015$/, "Poster for Warung's 13th anniversary, 2015")
                .replace(/^Cartaz dos 15 anos do Warung com o Watergate/, "Poster for Warung's 15th anniversary with Watergate")
                .replace(/^Cartaz de evento com Aninha no line-up$/, "Event poster with Aninha on the line-up")
                .replace(/^Cartaz (do|da|no) /, "Poster: ")
                .replace(/, junho de 2017$/, ", June 2017")
                .replace(/, dezembro de 2016$/, ", December 2016")
                .replace(/, maio de 2015$/, ", May 2015")
                .replace(/ em Berlim, /, " in Berlin, ")
                .replace(/ com Aninha, Ingrid e Dai Bohn/, " with Aninha, Ingrid and Dai Bohn")
                .replace(/ e /g, " and "),
    },
    es: {
        nav: ["Inicio", "Bio", "Discografía", "Mixes", "Agenda", "Contacto"],
        navMain: "Principal",
        skip: "Saltar al contenido",
        home: "Aninha, página de inicio",
        openMenu: "Abrir menú",
        closeMenu: "Cerrar menú",
        footer: "Pie de página",
        footerAlt: "Retrato en blanco y negro de Aninha",
        langs: "Idioma",
        siteTitle: "Aninha | DJ & Productora de Música Electrónica",
        labels: "Sellos discográficos",
        soon: "Nuevas fechas próximamente.",
        done: "Realizado",
        tickets: "Entradas ↗",
        months: ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"],
        locale: "es",
        watch: "Ver video",
        alt: (a: string) =>
            a
                .replace(/^Capa de lançamento da Aninha$/, "Portada de un lanzamiento de Aninha")
                .replace(/^Capa: /, "Portada: ")
                .replace(/^Cartaz dos 13 anos do Warung, 2015$/, "Afiche del 13.º aniversario de Warung, 2015")
                .replace(/^Cartaz dos 15 anos do Warung com o Watergate/, "Afiche del 15.º aniversario de Warung con Watergate")
                .replace(/^Cartaz de evento com Aninha no line-up$/, "Afiche de evento con Aninha en el line-up")
                .replace(/^Cartaz (do|da|no) /, "Afiche: ")
                .replace(/, junho de 2017$/, ", junio de 2017")
                .replace(/, dezembro de 2016$/, ", diciembre de 2016")
                .replace(/, maio de 2015$/, ", mayo de 2015")
                .replace(/ em Berlim, /, " en Berlín, ")
                .replace(/ com Aninha, Ingrid e Dai Bohn/, " con Aninha, Ingrid y Dai Bohn")
                .replace(/ e /g, " y "),
    },
} as const
