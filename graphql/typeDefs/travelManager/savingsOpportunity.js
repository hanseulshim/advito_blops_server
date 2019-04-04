exports.savingsOpportunityDefs = `
type SavingsOpportunityDetail {
  id: Int
  metricList: [SavingsOpportunityMetric]
  comments: [String]
}

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
`;

exports.savingsOpportunityQueries = `
savingsOpportunityDetail(id: Int!, filterId: Int): SavingsOpportunityDetail @auth
`;
