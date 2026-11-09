# aninha.art.br

Site oficial da Aninha, feito em [Astro](https://astro.build) e publicado na Vercel. Cada envio para o branch `main` publica o site sozinho.

## Onde mexer

- **Textos das páginas:** `src/pages/` (`index.astro`, `bio.astro`, `discografia.astro`, `mixes.astro`, `contato.astro`).
- **Menu, redes, gravadoras, capas e cartazes:** `src/data/site.ts`.
- **Lançamentos do Spotify:** lista `albums` em `src/pages/discografia.astro` (o código do álbum é o trecho depois de `/album/` no link do Spotify).
- **Mixes:** lista `mixes` em `src/pages/mixes.astro` (código do vídeo do YouTube ou o final do link do SoundCloud).
- **Formulário:** envia pelo FormSubmit para o e-mail definido em `src/pages/contato.astro`.
- **Imagens:** `public/img/`. **Vídeo do contato:** `public/video/`.

## Rodar no computador

```bash
npm install
npm run dev
```

A pasta `_ref/` guarda prints e o HTML do site antigo (Framer), só como referência da migração.
