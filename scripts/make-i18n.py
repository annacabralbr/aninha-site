# Gera as versões em inglês (src/pages/en/) e espanhol (src/pages/es/) a partir das
# páginas em português. Depois de mudar um texto em PT, atualize a tradução aqui e rode:
#   python3 scripts/make-i18n.py
# O script avisa e para se algum trecho em PT não for encontrado.
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = ["index.astro", "bio.astro", "discografia.astro", "mixes.astro", "agenda.astro", "contato.astro"]


def common(lang):
    return [
        ('from "../', 'from "../../'),
        ("<Base ", f'<Base lang="{lang}" '),
        ('href="/"', f'href="/{lang}/"'),
        ('href="/bio"', f'href="/{lang}/bio"'),
        ('href="/discografia"', f'href="/{lang}/discografia"'),
        ('href="/mixes"', f'href="/{lang}/mixes"'),
        ('href="/agenda"', f'href="/{lang}/agenda"'),
        ('href="/contato"', f'href="/{lang}/contato"'),
        ("<AgendaList ", f'<AgendaList lang="{lang}" '),
        ("<YouTube ", f'<YouTube lang="{lang}" '),
        ("<Labels />", f'<Labels lang="{lang}" />'),
        ("<CoverWall ", f'<CoverWall lang="{lang}" '),
        ("https://aninha.art.br/contato?enviado=1", f"https://aninha.art.br/{lang}/contato?enviado=1"),
    ]


BIO_PT = [
    "Aninha personifica essa essência: DJ, produtora musical, empresária e impulsionadora do cenário eletrônico, cuja trajetória de 20 anos redefine o panorama musical brasileiro.",
    "A garota catarinense, radicada em Curitiba, tinha o desejo de viver da música e quebrou barreiras como pioneira no cenário feminino da música eletrônica no Brasil.",
    "Sua jornada a levou de norte a sul, deixando sua marca sonora singular como DJ residente em pistas renomadas como Warung Beach Club, Club Vibe e D-Edge.",
    "Aninha é mais do que uma DJ, é uma artista que tece uma narrativa sonora, mergulhando profundamente em pesquisas musicais e explorando estilos incomuns.",
    "Sua residência no Warung por mais de uma década e a presença constante em clubs renomados testemunham sua habilidade de construir conceitos sonoros vanguardistas.",
    "Desde 2019, é residente do grupo D-Edge / Surreal, reforçando sua atuação em projetos inovadores e de grande prestígio no cenário nacional.",
    "Seu talento e profissionalismo a consolidaram como uma das maiores DJs da história da música eletrônica brasileira, com participação em line-ups de renome nacional e internacional.",
    "Além dos palcos, Aninha integrou projetos de sucesso como a AIA Records, gravadora que completa 10 anos impulsionando não apenas suas produções, mas também talentos nacionais, exportando cultura de pista de dança para o mundo.",
    "Duas décadas se passaram, mas o espírito vanguardista de Aninha permanece vibrante. Sua busca constante por inovação a estabelece como fonte de inspiração para as gerações futuras de mulheres na música eletrônica.",
]
BIO = {
    "en": [
        "Aninha embodies this essence: DJ, music producer, entrepreneur and driving force in the electronic scene, whose 20-year journey has reshaped Brazil's music landscape.",
        "Born in Santa Catarina and based in Curitiba, she set out to make a living from music and broke barriers as a pioneer for women in Brazilian electronic music.",
        "Her journey took her from north to south, leaving her unique sonic signature as a resident DJ at renowned dance floors such as Warung Beach Club, Club Vibe and D-Edge.",
        "Aninha is more than a DJ: she is an artist who weaves a sonic narrative, digging deep into music research and exploring unusual styles.",
        "Her residency at Warung for more than a decade and her constant presence at renowned clubs show her ability to build forward-thinking sonic concepts.",
        "Since 2019 she has been a resident of the D-Edge / Surreal group, strengthening her work in innovative, highly regarded projects across Brazil.",
        "Her talent and professionalism have established her as one of the greatest DJs in the history of Brazilian electronic music, playing on national and international line-ups.",
        "Beyond the booth, Aninha has been part of successful projects such as AIA Records, a label celebrating 10 years of pushing not only her own productions but also Brazilian talent, exporting dance floor culture to the world.",
        "Two decades on, Aninha's forward-thinking spirit is still vibrant. Her constant search for innovation makes her a source of inspiration for future generations of women in electronic music.",
    ],
    "es": [
        "Aninha encarna esa esencia: DJ, productora musical, empresaria e impulsora de la escena electrónica, cuya trayectoria de 20 años redefine el panorama musical brasileño.",
        "Nacida en Santa Catarina y radicada en Curitiba, quería vivir de la música y rompió barreras como pionera de las mujeres en la música electrónica de Brasil.",
        "Su camino la llevó de norte a sur, dejando su sello sonoro como DJ residente en pistas reconocidas como Warung Beach Club, Club Vibe y D-Edge.",
        "Aninha es más que una DJ: es una artista que teje una narrativa sonora, con una investigación musical profunda y estilos poco comunes.",
        "Su residencia en Warung durante más de una década y su presencia constante en clubes reconocidos muestran su capacidad para construir conceptos sonoros de vanguardia.",
        "Desde 2019 es residente del grupo D-Edge / Surreal, reforzando su presencia en proyectos innovadores y de gran prestigio en Brasil.",
        "Su talento y profesionalismo la consolidaron como una de las DJs más importantes de la historia de la música electrónica brasileña, con presencia en line-ups nacionales e internacionales.",
        "Más allá de la cabina, Aninha formó parte de proyectos exitosos como AIA Records, sello que cumple 10 años impulsando no solo sus producciones, sino también talentos brasileños, exportando la cultura de la pista de baile al mundo.",
        "Pasaron dos décadas y el espíritu de vanguardia de Aninha sigue vivo. Su búsqueda constante de innovación la convierte en inspiración para las próximas generaciones de mujeres en la música electrónica.",
    ],
}

CAREER = [  # papel em PT -> EN, ES
    ('"DJ residente"', '"Resident DJ"', '"DJ residente"'),
    ('"Artista exclusiva"', '"Exclusive artist"', '"Artista exclusiva"'),
    ('"Sócia fundadora"', '"Founding partner"', '"Socia fundadora"'),
    ('"Sócia idealizadora"', '"Co-creator and partner"', '"Socia creadora"'),
    ('"Idealizadora"', '"Creator"', '"Creadora"'),
    ('"Fundadora"', '"Founder"', '"Fundadora"'),
    ('"Bolívia"', '"Bolivia"', '"Bolivia"'),
    ('"Colômbia"', '"Colombia"', '"Colombia"'),
    ('"Estados Unidos"', '"United States"', '"Estados Unidos"'),
    ('"Argentina"', '"Argentina"', '"Argentina"'),
    ('"Peru"', '"Peru"', '"Perú"'),
    ('"Europa"', '"Europe"', '"Europa"'),
    ('"Tour"', '"Tour"', '"Tour"'),
    ("hoje", "present", "hoy"),
]

T = {
    "index.astro": [
        ('description="Site oficial da artista. Confira os lançamentos, informações, sets e contato para bookings."', 'description="Official website. Releases, bio, sets and booking contact."', 'description="Sitio oficial de la artista. Lanzamientos, bio, sets y contacto para bookings."'),
        ('alt="Retrato em preto e branco da Aninha"', 'alt="Black and white portrait of Aninha"', 'alt="Retrato en blanco y negro de Aninha"'),
        ("DJ baseada em Curitiba PR,", "DJ based in Curitiba, Brazil,", "DJ radicada en Curitiba, Brasil,"),
        ("Responsável por moldar a identidade sonora de clubs como Warung, Club Vibe e Terraza.", "Shaping the sound identity of clubs such as Warung, Club Vibe and Terraza.", "Responsable de dar forma a la identidad sonora de clubes como Warung, Club Vibe y Terraza."),
        ("Com mais de 20 anos de pista, Aninha foi residente de longa data no Warung Beach Club e no Club Vibe, além de integrar o ecossistema D-Edge e o Surreal Park desde 2019.", "With more than 20 years on the dance floor, Aninha was a long-time resident at Warung Beach Club and Club Vibe, and has been part of the D-Edge and Surreal Park ecosystem since 2019.", "Con más de 20 años de pista, Aninha fue residente durante años en Warung Beach Club y Club Vibe, y forma parte del ecosistema D-Edge y Surreal Park desde 2019."),
        ('alt="Aninha tocando para a pista lotada, vista de trás da cabine"', 'alt="Aninha playing to a packed dance floor, seen from behind the booth"', 'alt="Aninha tocando para una pista llena, vista desde detrás de la cabina"'),
        ("Aninha é referência sul-americana quando o assunto é warm up: pesquisadora, pioneira e especialista em criar atmosferas que transitam do house ao techno com precisão.", "Aninha is a South American reference in warm-up sets: a digger, a pioneer and a specialist in building atmospheres that move from house to techno with precision.", "Aninha es referencia sudamericana en warm up: investigadora, pionera y especialista en crear atmósferas que van del house al techno con precisión."),
        ('aria-label="Próximas datas"', 'aria-label="Upcoming dates"', 'aria-label="Próximas fechas"'),
        ('label="/ Agenda" title="Próximas datas"', 'label="/ Tour dates" title="Upcoming dates"', 'label="/ Agenda" title="Próximas fechas"'),
        ("<span>Agenda completa</span>\n                        <span aria-hidden=\"true\">Agenda completa</span>", "<span>All dates</span>\n                        <span aria-hidden=\"true\">All dates</span>", "<span>Agenda completa</span>\n                        <span aria-hidden=\"true\">Agenda completa</span>"),
        ('aria-label="Lançamentos"', 'aria-label="Releases"', 'aria-label="Lanzamientos"'),
        ('label="/ Lançamentos" title="Albuns, EPs & remixes"', 'label="/ Releases" title="Albums, EPs & remixes"', 'label="/ Lanzamientos" title="Álbumes, EPs & remixes"'),
        ('label="Capas de lançamentos"', 'label="Release covers"', 'label="Portadas de lanzamientos"'),
        ('label="/Mixes" title="Mixes gravados ao vivo & estúdio"', 'label="/Mixes" title="Live & studio mixes"', 'label="/Mixes" title="Mixes en vivo & estudio"'),
        ('aria-label="Ouvir os mixes"', 'aria-label="Listen to the mixes"', 'aria-label="Escuchar los mixes"'),
    ],
    "bio.astro": [(f'"{p}"', f'"{e}"', f'"{s}"') for p, e, s in zip(BIO_PT, BIO["en"], BIO["es"])]
    + CAREER
    + [
        ('description="Biografia da Aninha: 20 anos de pista, residências no Warung, Club Vibe e D-Edge, gravadoras e turnês."', 'description="Aninha\'s biography: 20 years on the dance floor, residencies at Warung, Club Vibe and D-Edge, labels and tours."', 'description="Biografía de Aninha: 20 años de pista, residencias en Warung, Club Vibe y D-Edge, sellos y giras."'),
        ('label="/ Bio" title="Aninha é mais do que uma DJ, é uma artista que tece uma narrativa sonora"', 'label="/ Bio" title="Aninha is more than a DJ, she is an artist who weaves a sonic narrative"', 'label="/ Bio" title="Aninha es más que una DJ, es una artista que teje una narrativa sonora"'),
        ('alt="Aninha de braço erguido na cabine, de frente para a pista lotada"', 'alt="Aninha with her arm raised in the booth, facing a packed dance floor"', 'alt="Aninha con el brazo en alto en la cabina, frente a una pista llena"'),
        ('alt="Aninha e outro DJ na cabine do Surreal diante da pista cheia"', 'alt="Aninha and another DJ in the Surreal booth in front of a full dance floor"', 'alt="Aninha y otro DJ en la cabina de Surreal frente a la pista llena"'),
        ("Em um mundo em constante evolução, Aninha é um farol, sempre mirando ao novo, à mudança, ao bem e para o melhor. Seu porto seguro reside nela mesma, onde sua música e coração encontram significado e autenticidade.", "In a constantly changing world, Aninha is a beacon, always looking to the new, to change, to the good and to the better. Her safe harbor lies within herself, where her music and her heart find meaning and authenticity.", "En un mundo en constante evolución, Aninha es un faro, siempre mirando a lo nuevo, al cambio, al bien y a lo mejor. Su refugio está en ella misma, donde su música y su corazón encuentran sentido y autenticidad."),
        ('aria-label="História"', 'aria-label="Career"', 'aria-label="Historia"'),
        ('label="/História" title="Carreira sólida"', 'label="/Career" title="A solid career"', 'label="/Historia" title="Una carrera sólida"'),
        ('<caption class="sr-only">Linha do tempo da carreira</caption>', '<caption class="sr-only">Career timeline</caption>', '<caption class="sr-only">Línea de tiempo de la carrera</caption>'),
        ('<th scope="col">Período</th><th scope="col">Onde</th><th scope="col">Papel</th>', '<th scope="col">Period</th><th scope="col">Where</th><th scope="col">Role</th>', '<th scope="col">Período</th><th scope="col">Dónde</th><th scope="col">Rol</th>'),
        ('aria-label="Principais gravadoras"', 'aria-label="Main record labels"', 'aria-label="Principales sellos"'),
        ("/ Principais gravadoras", "/ Main record labels", "/ Principales sellos"),
        ('label="Cartazes de eventos"', 'label="Event posters"', 'label="Afiches de eventos"'),
    ],
    "discografia.astro": [
        ('title="Discografia" description="Confira os lançamentos da Aninha: álbuns, EPs e remixes."', 'title="Discography" description="Aninha\'s releases: albums, EPs and remixes."', 'title="Discografía" description="Lanzamientos de Aninha: álbumes, EPs y remixes."'),
        ('label="/ Discografia" title="Confira os últimos lançamentos"', 'label="/ Discography" title="Latest releases"', 'label="/ Discografía" title="Últimos lanzamientos"'),
        ('title="Lançamento em destaque no Spotify"', 'title="Featured release on Spotify"', 'title="Lanzamiento destacado en Spotify"'),
        ("title={`Lançamento ${i + 2} no Spotify`}", "title={`Release ${i + 2} on Spotify`}", "title={`Lanzamiento ${i + 2} en Spotify`}"),
        ("<span>Mostrar no Spotify ↗</span><span aria-hidden=\"true\">Mostrar no Spotify ↗</span>", "<span>More on Spotify ↗</span><span aria-hidden=\"true\">More on Spotify ↗</span>", "<span>Más en Spotify ↗</span><span aria-hidden=\"true\">Más en Spotify ↗</span>"),
        ("<span>Mostrar no Beatport ↗</span><span aria-hidden=\"true\">Mostrar no Beatport ↗</span>", "<span>More on Beatport ↗</span><span aria-hidden=\"true\">More on Beatport ↗</span>", "<span>Más en Beatport ↗</span><span aria-hidden=\"true\">Más en Beatport ↗</span>"),
    ],
    "mixes.astro": [
        ('description="Mixes da Aninha gravados ao vivo e em estúdio."', 'description="Aninha\'s live and studio mixes."', 'description="Mixes de Aninha grabados en vivo y en estudio."'),
        ('label="/Mixes" title="Mixes gravados ao vivo & estúdio"', 'label="/Mixes" title="Live & studio mixes"', 'label="/Mixes" title="Mixes en vivo & estudio"'),
        ("<span>Mais sets no SoundCloud ↗</span><span aria-hidden=\"true\">Mais sets no SoundCloud ↗</span>", "<span>More sets on SoundCloud ↗</span><span aria-hidden=\"true\">More sets on SoundCloud ↗</span>", "<span>Más sets en SoundCloud ↗</span><span aria-hidden=\"true\">Más sets en SoundCloud ↗</span>"),
    ],
    "agenda.astro": [
        ('title="Agenda" description="Agenda de apresentações da Aninha: próximas datas e datas anteriores."', 'title="Tour dates" description="Aninha\'s tour dates: upcoming and past shows."', 'title="Agenda" description="Agenda de presentaciones de Aninha: próximas fechas y fechas anteriores."'),
        ('label="/ Agenda" title="Próximas datas"', 'label="/ Tour dates" title="Upcoming dates"', 'label="/ Agenda" title="Próximas fechas"'),
    ],
    "contato.astro": [
        ('title="Contato" description="Contato, agenda e bookings da Aninha."', 'title="Contact" description="Contact and bookings for Aninha."', 'title="Contacto" description="Contacto, agenda y bookings de Aninha."'),
        ("Contato, agenda & dúvidas", "Contact, bookings & questions", "Contacto, agenda & dudas"),
        ("Mensagem enviada. Obrigada! Respondo assim que puder.", "Message sent. Thank you! I'll reply as soon as I can.", "Mensaje enviado. ¡Gracias! Respondo lo antes posible."),
        ('<legend class="sr-only">Tipo de contato</legend>', '<legend class="sr-only">Type of contact</legend>', '<legend class="sr-only">Tipo de contacto</legend>'),
        ("<span>Pessoal</span>", "<span>Personal</span>", "<span>Personal</span>"),
        ("<span>Comercial</span>", "<span>Business</span>", "<span>Comercial</span>"),
        ('value="Contato pelo site aninha.art.br"', 'value="Contact from aninha.art.br (EN)"', 'value="Contacto desde aninha.art.br (ES)"'),
        ('<span class="s">Nome*</span>', '<span class="s">Name*</span>', '<span class="s">Nombre*</span>'),
        ('placeholder="qual seu nome?"', 'placeholder="your name"', 'placeholder="¿cuál es tu nombre?"'),
        ('placeholder="qual seu insta?"', 'placeholder="your instagram"', 'placeholder="¿cuál es tu insta?"'),
        ('placeholder="escreva seu melhor email"', 'placeholder="your best email"', 'placeholder="tu mejor email"'),
        ('<span class="s">Cidade</span>', '<span class="s">City</span>', '<span class="s">Ciudad</span>'),
        ('placeholder="qual sua cidade?"', 'placeholder="your city"', 'placeholder="¿de qué ciudad eres?"'),
        ('<span class="s">Mensagem*</span>', '<span class="s">Message*</span>', '<span class="s">Mensaje*</span>'),
        ('placeholder="escreva sua mensagem :)"', 'placeholder="write your message :)"', 'placeholder="escribe tu mensaje :)"'),
        ("                    Enviar\n", "                    Send\n", "                    Enviar\n"),
    ],
}

missing = False
for lang, idx in (("en", 1), ("es", 2)):
    for page in PAGES:
        src = open(os.path.join(ROOT, "src/pages", page), encoding="utf8").read()
        out = src
        for a, b in common(lang):
            out = out.replace(a, b)
        for row in T.get(page, []):
            a, b = row[0], row[idx]
            if a not in out:
                print(f"[{lang}/{page}] trecho não encontrado: {a[:70]}")
                missing = True
                continue
            out = out.replace(a, b)
        dst = os.path.join(ROOT, "src/pages", lang, page)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        open(dst, "w", encoding="utf8").write(out)
if missing:
    sys.exit(1)
print("ok")
