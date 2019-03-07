const {
  programPerformanceListTravel,
  netSpendAnalysisListTravel,
  personaList,
  savingsOpportunityList,
  riskAreaList,
  noChangeSince,
} = require('../../../data/travelManager/dashboard');

exports.dashboardQueries = {
  programPerformanceListTravel: () => programPerformanceListTravel,
  netSpendAnalysisListTravel: () => netSpendAnalysisListTravel,
  personaList: () => personaList,
  savingsOpportunityFeedTravel: (
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
  riskAreaFeedTravel: (_, { limit = riskAreaList.length, cursor = 0 }) => {
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
  noChangeSince: () => noChangeSince,
};
