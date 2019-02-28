const { generateType } = require('../helper')

exports.savingsOpportunityDetailDefs = `
${generateType(
  'SavingsOpportunityDetail',
  `{
    id: Int
    metricList: [SavingsOpportunityMetric]
    comments: [String],
}`,
)}

type SavingsOpportunityMetric {
  title: String
  personaList: [SavingsOpportunityPersona]
}

type SavingsOpportunityPersona {
  title: String
  value: Float
  hover: SavingsOpportunityHover
}

type SavingsOpportunityHover {
  fields: [SavingsOpportunityField]
  comments: [String]
}

type SavingsOpportunityField {
  name: String,
  value: String
}
`

exports.savingsOpportunityDetailQuery = `
  savingsOpportunityDetail(sessionToken: String!, id: Int!): SavingsOpportunityDetail
`
