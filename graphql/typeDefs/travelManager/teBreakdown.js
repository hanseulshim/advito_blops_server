exports.teBreakdownDefs = `

type teBreakdownDetail {
  wifiBenchmark:Float,
  mealsBenchmark:Float,
  travelBenchmark:Float,
  lodgingBenchmark:Float,
  personas: [TePersona]
}

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
    icon: String
}

`;

exports.teBreakdownQueries = `
teBreakdownDetail( filterId: Int): teBreakdownDetail @auth`;
