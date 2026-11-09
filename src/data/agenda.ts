// Agenda de apresentações. Adicione uma linha por data, em qualquer ordem: o site
// organiza da mais nova para a mais antiga e deixa as que já passaram com 50% de opacidade.
// data: "AAAA-MM-DD" · cidade · local (club ou festa) · evento (opcional) · link (ingressos, opcional)
export type Show = { data: string; cidade: string; local: string; evento?: string; link?: string }

export const AGENDA: Show[] = []
