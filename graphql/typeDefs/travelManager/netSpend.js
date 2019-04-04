exports.netSpendDefs = `
type NetSpendDetail {
    spendCategories: [SpendCategory]
    projectedSpend: [ProjectedField]
    actualSpend: [ActualField]
    summary: Summary
}

type SpendCategory {
    title: String,
    icon: String,
    amount: String,
    diff: Float
}

type ProjectedField { 
    date: String,
    spend: Float
}

type ActualField {
    date: String,
    spend:Float
}

type Summary {
    title: String,
    info: String
}
`;

exports.netSpendQueries = `
  netSpendDetail( filterId: Int): NetSpendDetail @auth
`;
