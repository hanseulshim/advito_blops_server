exports.dashboardDefs = `
type ProgramPerformanceExecutive {
  value: String
}
type NetSpendAnalysisExecutive {
  date: String
  value: Float
  projValue: Float
}
type Division {
  title: String
  value: String
  programShare: Int
}
`;

exports.dashboardQueries = `
  programPerformanceExecutive(filterId: Int): ProgramPerformanceExecutive @auth
  netSpendAnalysisListExecutive(filterId: Int): [NetSpendAnalysisExecutive] @auth
  divisionListExecutive(filterId: Int): [Division] @auth
  savingsOpportunityFeedExecutive(limit: Int, cursor: Int, filterId: Int): SavingsOpportunityFeed @auth
  riskAreaFeedExecutive(limit: Int, cursor: Int, filterId: Int): RiskAreaFeed @auth
`;
