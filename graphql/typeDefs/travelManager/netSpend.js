exports.netSpendDefs = `
type NetSpendDetail {
    spendCategories: [SpendCategory]
    spend: [Spend]
    summary: Summary
}

type SpendCategory {
    title: String,
    icon: String,
    amount: String,
    diff: Float
}

type Spend { 
    date: String,
    projSpend: Float,
    actualSpend: Float,
    delta: Float
    color: String
}

type Summary {
    title: String,
    info: String
}
`;

exports.netSpendQueries = `
  netSpendDetail( filterId: Int): NetSpendDetail @auth
`;
