exports.dashboardDefs = `
type ProgramPerformanceTravel {
  id: Int
  title: String
  value: String
  unit: String
}
type NetSpendAnalysisTravel {
  date: String
  value: Float
  projValue: Float
}
type Persona {
  title: String
  value: String
  programShare: Int
}
type SavingsOpportunityFeed {
  prevCursor: Int
  cursor: Int
  totalSavingsOpportunities: Int
  hasNext: Boolean
  savingsOpportunityList: [SavingsOpportunity]
}
type SavingsOpportunity {
  id: Int
  title: String
  value: String
  unit: String
  secondaryValue: String
  secondaryUnit: String
  divisionList: [SavingsOpportunityDivision]
}
type SavingsOpportunityDivision {
  title: String,
  value: String,
  secondaryValue: String,
  unit: String,
  secondaryUnit: String,
}
type RiskAreaFeed {
  prevCursor: Int
  cursor: Int
  totalRiskAreas: Int
  hasNext: Boolean
  riskAreaList: [RiskArea]
}
type RiskArea {
  id: Int
  title: String
  value: String
  unit: String
  secondaryValue: String
  secondaryUnit: String
  divisionList: [RiskAreaDivision]
}
type RiskAreaDivision {
  title: String,
  value: String,
  secondaryValue: String,
  unit: String,
  secondaryUnit: String,
}
`;

exports.dashboardQueries = `
  programPerformanceListTravel(filterId: Int): [ProgramPerformanceTravel] @auth
  netSpendAnalysisListTravel(filterId: Int): [NetSpendAnalysisTravel] @auth
  personaList(filterId: Int): [Persona] @auth
  savingsOpportunityFeedTravel(limit: Int, cursor: Int, filterId: Int): SavingsOpportunityFeed @auth
  riskAreaFeedTravel(limit: Int, cursor: Int, filterId: Int): RiskAreaFeed @auth
  noChangeSince(filterId: Int): String @auth
`;
