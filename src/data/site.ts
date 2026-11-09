// Links do menu e das redes, usados no topo e no rodapé.
export const NAV = [
    { href: "/", label: "Início" },
    { href: "/bio", label: "Bio" },
    { href: "/discografia", label: "Discografia" },
    { href: "/mixes", label: "Mixes" },
    { href: "/agenda", label: "Agenda" },
    { href: "/contato", label: "Contato" },
]
export const SOCIAL = [
    { href: "https://www.beatport.com/artist/aninha/106303", label: "Beatport" },
    { href: "https://www.youtube.com/@aninhamusic", label: "YouTube" },
    { href: "https://www.instagram.com/aninha.music", label: "Instagram" },
    { href: "https://www.danceart.com.br/contato", label: "Dance Art Bookings" },
]
export const LABELS = ["Nervous", "Nite Grooves", "Kings Street", "Defected", "Wow!", "Warung Rec"]

// Capas da home (três faixas) e cartazes da bio (três faixas), na ordem do site antigo.
const I = (f: string, alt: string) => ({ src: `/img/${f}`, alt })
export const COVERS = [
    [
        I("xWjKAaxjT6tHzM7RGolqNwWrc.png", "Capa de lançamento da Aninha"),
        I("4zbrCai85A6uDo0ibAlBrC1gSg.png", "Capa: Fabø e Aninha, Filter Cuts / Sunny Breaks, Nervous Records"),
        I("hqF180bKnNOgyhfK7HzwUwCFHo.png", "Capa: Aninha vs. Antonela Giampietro e Dub Recycle, Change All EP"),
        I("nWNJcpqjr6hvIAfYoW0NAgPoGs.png", "Capa: Fabø e Aninha, Scancione"),
        I("O3srm5K0VAp4X9Dkj0XvbCvWxE.png", "Capa: Brava Brazil, Warung"),
    ],
    [
        I("BiJFWoU6fV7InSnjTFtV7H7As.png", "Capa: Aninha e Fabø, Pyramid, WOW!"),
        I("wTno68e7dR9Va5MevAik4KnK0.png", "Capa: Aninha e Fabø, Circles EP"),
        I("cjg6Ib5vB4eNhKrMdadDC8A3OQ.png", "Capa: Aninha vs. Antonela Giampietro, Le Poème EP"),
        I("uyoUGUFYgc4msiSw2vgXbbMqv8.png", "Capa: Aninha vs. Antonela Giampietro, Lost / Feelings, remix de Moe Turk"),
        I("o7P6kNwAX99nywgoua8Nn1vEA.png", "Capa: Sampler View vol. 2"),
    ],
    [
        I("WS74HIM4EF4RlmxeMy2RCfWWE.png", "Capa: Soulcuts, Priority"),
        I("0fCABWqOcUYxVkDSWCnFv90iHYw.png", "Capa: Bluebook, Aninha"),
        I("TS8GF67QdlkCzFKzzSS5bnXUSyg.png", "Capa: Fabø e Aninha, Nervous Records"),
        I("JKd8sYJbuAuOgqAF7WFk198ZPI.png", "Capa: WOW! Va Summer"),
        I("y0AYd4Z1vvpCabt6ytM1sJn4yl4.png", "Capa: Music Comes First EP"),
    ],
]
export const POSTERS = [
    [
        I("ClrVA2aHC10Ol3JAM5j7920OY.jpg", "Cartaz do Time Warp São Paulo"),
        I("00Ko9DAcgVGpAAkrerBodgDYc.jpg", "Cartaz dos 13 anos do Warung, 2015"),
        I("KEaPjIRFwJiFJbMujEw9SWwdlQ.jpg", "Cartaz do Tribe Club"),
        I("asaloyITg737B51n9RzZ9xeM.jpg", "Cartaz no D-Edge com Aninha, Ingrid e Dai Bohn"),
        I("5PVB37LGIMIurwAvBtJAkT61zY.jpg", "Cartaz do Warung Beach Club, maio de 2015"),
    ],
    [
        I("aagolg7dXpdobLhJCWkh1FLcJK4.jpg", "Cartaz do BPM no Surreal"),
        I("ZqrQsnCL43dchO3lowKj9p9Teo.jpg", "Cartaz do Elrow Sambódromo do Brasil"),
        I("reFwdMDsljL7oaK0h6YssMM7aQU.jpg", "Cartaz de evento com Aninha no line-up"),
        I("D76dlsijVtCBsGqA10CR648ddHY.jpg", "Cartaz dos 15 anos do Warung com o Watergate, junho de 2017"),
        I("WA5jMmydlGzlp9PGlhA6EEqnoY.jpg", "Cartaz do Warung, dezembro de 2016"),
    ],
    [
        I("eTp45JlnRdxIx6ohHd2i4ko6E8.jpg", "Cartaz do Warung Day Festival"),
        I("pCaSO7J7BOgvBVPI340LfvjkXc.jpg", "Cartaz do Monza Ibiza Records Showcase"),
        I("hB5Vqwf9sM80QjVpvSBfcSAfQE.jpg", "Cartaz do The BPM Festival Brasil, 2017"),
        I("QBZ6Uk56ovRlCGA8Jk7x4QIq3fU.jpg", "Cartaz do Elrow Bollywood"),
        I("7Gr1cHDErbdidlmDXvhUrZupeBo.jpg", "Cartaz dos 15 anos do Warung com o Watergate em Berlim, 2017"),
    ],
]
