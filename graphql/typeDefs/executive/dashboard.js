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
  programPerformanceExecutive: ProgramPerformanceExecutive @auth
  netSpendAnalysisListExecutive: [NetSpendAnalysisExecutive] @auth
  marketList: [Market] @auth
  savingsOpportunityFeedExecutive(limit: Int, cursor: Int): SavingsOpportunityFeed @auth
  riskAreaFeedExecutive(limit: Int, cursor: Int): RiskAreaFeed @auth
`;
