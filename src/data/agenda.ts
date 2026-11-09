// Agenda de apresentações. Adicione uma linha por data, em qualquer ordem: o site
// organiza da mais nova para a mais antiga e deixa as que já passaram com 50% de opacidade.
// data: "AAAA-MM-DD" · cidade · local (club ou festa) · evento (opcional) · link (ingressos, opcional)
export type Show = { data: string; cidade: string; local: string; evento?: string; link?: string }

export const AGENDA: Show[] = [
    { data: "2026-08-15", cidade: "Joinville, SC", local: "Fuse" },
    { data: "2026-08-21", cidade: "Balneário Camboriú, SC", local: "Lo-Fi" },
    { data: "2026-08-22", cidade: "Lages, SC", local: "Surreal Tour" },
    { data: "2026-10-10", cidade: "Curitiba, PR", local: "Club Vibe", evento: "Marola Grooves" },
    { data: "2026-10-11", cidade: "Garopaba, SC", local: "Kumaras" },
    { data: "2026-10-31", cidade: "Blumenau, SC", local: "D.O.C.K" },
    { data: "2026-11-07", cidade: "Ponta Grossa, PR", local: "Cavan 77" },
    { data: "2026-11-13", cidade: "Rio de Janeiro, RJ", local: "D-Edge", evento: "Tulipa" },
    { data: "2026-11-14", cidade: "Curitiba, PR", local: "Kirin", evento: "First Class" },
    { data: "2026-11-19", cidade: "Itajaí, SC", local: "Isla Praia Brava" },
    { data: "2026-12-04", cidade: "Goiânia, GO", local: "Offspot", evento: "V0lar5" },
    { data: "2026-12-12", cidade: "Curitiba, PR", local: "+55", evento: "Surreal Tour" },
    { data: "2026-12-17", cidade: "Curitiba, PR", local: "Macro", evento: "Escuta" },
    { data: "2026-12-27", cidade: "Florianópolis, SC", local: "Terraza" },
    { data: "2026-12-28", cidade: "Garopaba, SC", local: "Kumaras" },
    { data: "2026-12-31", cidade: "Florianópolis, SC", local: "Réveillon Troop" },
    { data: "2027-01-30", cidade: "Campo Largo, PR", local: "PVT" },
]
