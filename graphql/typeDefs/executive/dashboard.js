exports.dashboardDefs = `
type ProgramPerformanceExecutive {
  value: String
}
type NetSpendAnalysisExecutive {
  date: String
  value: Float
}
type Market {
  title: String
  value: String
  programShare: Int
}
`;

exports.dashboardQueries = `
  programPerformanceExecutive(filterId: Int): ProgramPerformanceExecutive @auth
  netSpendAnalysisListExecutive(filterId: Int): [NetSpendAnalysisExecutive] @auth
  marketList(filterId: Int): [Market] @auth
  savingsOpportunityFeedExecutive(limit: Int, cursor: Int, filterId: Int): SavingsOpportunityFeed @auth
  riskAreaFeedExecutive(limit: Int, cursor: Int, filterId: Int): RiskAreaFeed @auth
`;
