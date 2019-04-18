exports.teBreakdownDefs = `

type TePersona {
    title: String,
    description: String,
    programShare: Float,
    totalTripCost: Float,
    totalTripCostDelta: Float,
    data: [PersonaSpend]
}

type PersonaSpend {
    name: String,
    value: Float,
    delta: Float,
    title: String,
    description: String,
    icon: String,
    benchmark: Float
}

`;

exports.teBreakdownQueries = `
teBreakdownDetail( filterId: Int, view: String): [TePersona] @auth`;
