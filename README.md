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

## Inglês e espanhol

As páginas em `src/pages/en/` e `src/pages/es/` são geradas a partir das páginas em português. Depois de mudar um texto em PT, atualize a tradução em `scripts/make-i18n.py` e rode `python3 scripts/make-i18n.py`. Os textos do menu, rodapé e agenda ficam em `src/i18n.ts`. A agenda (`src/data/agenda.ts`) vale para os três idiomas.
