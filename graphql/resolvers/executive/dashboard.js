const {
  programPerformanceExecutive,
  netSpendAnalysisListExecutive,
  marketList,
  savingsOpportunityList,
  riskAreaList,
} = require('../../../data/executive/dashboard');

exports.dashboardQueries = {
  programPerformanceExecutive: () => programPerformanceExecutive,
  netSpendAnalysisListExecutive: () => netSpendAnalysisListExecutive,
  marketList: () => marketList,
  savingsOpportunityFeedExecutive: (
    _,
    { limit = savingsOpportunityList.length, cursor = 0 },
  ) => {
    const totalSavingsOpportunities = savingsOpportunityList.length;
    const newCursor = cursor + limit;
    const prevCursor = cursor - limit < 0 ? 0 : cursor - limit;
    return {
      prevCursor,
      cursor: newCursor,
      totalSavingsOpportunities,
      hasNext: newCursor < totalSavingsOpportunities,
      savingsOpportunityList: savingsOpportunityList.slice(cursor, newCursor),
    };
  },
  riskAreaFeedExecutive: (_, { limit = riskAreaList.length, cursor = 0 }) => {
    const totalRiskAreas = riskAreaList.length;
    const newCursor = cursor + limit;
    const prevCursor = cursor - limit < 0 ? 0 : cursor - limit;
    return {
      prevCursor,
      cursor: newCursor,
      totalRiskAreas,
      hasNext: newCursor < totalRiskAreas,
      riskAreaList: riskAreaList.slice(cursor, newCursor),
    };
  },
};
