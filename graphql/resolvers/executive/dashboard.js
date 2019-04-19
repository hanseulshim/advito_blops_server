const {
  programPerformanceExecutive,
  divisionList,
  netSpendAnalysisListExecutive,
  savingsOpportunityList,
  riskAreaList,
} = require('../../../data/executive/dashboard');

exports.dashboardQueries = {
  programPerformanceExecutive: (_, { filterId }) => {
    if (filterId) {
      programPerformanceExecutive.value = Math.floor(Math.random() * 87) / 10;
    }
    return programPerformanceExecutive;
  },
  netSpendAnalysisListExecutive: (_, { filterId }) => {
    if (filterId) {
      return netSpendAnalysisListExecutive.map(v => ({
        ...v,
        value: v.value * Math.floor(Math.random() * 15),
        projValue: v.projValue * Math.floor(Math.random() * 15),
      }));
    }
    return netSpendAnalysisListExecutive;
  },
  divisionListExecutive: (_, { filterId }) => {
    if (filterId) {
      return divisionList.map(v => ({
        ...v,
        value: `${Math.floor(Math.random() * 100) / 10}`,
        programShare: Math.floor(Math.random() * 100),
      }));
    }
    return divisionList;
  },
  savingsOpportunityFeedExecutive: (
    _,
    { limit = savingsOpportunityList.length, cursor = 0, filterId }
  ) => {
    const totalSavingsOpportunities = savingsOpportunityList.length;
    const newCursor = cursor + limit;
    const prevCursor = cursor - limit < 0 ? 0 : cursor - limit;
    if (filterId) {
      return {
        prevCursor,
        cursor: newCursor,
        totalSavingsOpportunities,
        hasNext: newCursor < totalSavingsOpportunities,
        savingsOpportunityList: savingsOpportunityList.slice(cursor, newCursor).map(v => ({
          ...v,
          value: `${Math.floor(Math.random() * 100)}%`,
        })),
      };
    }
    return {
      prevCursor,
      cursor: newCursor,
      totalSavingsOpportunities,
      hasNext: newCursor < totalSavingsOpportunities,
      savingsOpportunityList: savingsOpportunityList.slice(cursor, newCursor),
    };
  },
  riskAreaFeedExecutive: (_, { limit = riskAreaList.length, cursor = 0, filterId }) => {
    const totalRiskAreas = riskAreaList.length;
    const newCursor = cursor + limit;
    const prevCursor = cursor - limit < 0 ? 0 : cursor - limit;
    if (filterId) {
      return {
        prevCursor,
        cursor: newCursor,
        totalRiskAreas,
        hasNext: newCursor < totalRiskAreas,
        riskAreaList: riskAreaList.slice(cursor, newCursor).map(v => ({
          ...v,
          value: `${Math.floor(Math.random() * 100)}%`,
          secondaryValue: `$${Math.floor(Math.random() * 900)}K`,
        })),
      };
    }
    return {
      prevCursor,
      cursor: newCursor,
      totalRiskAreas,
      hasNext: newCursor < totalRiskAreas,
      riskAreaList: riskAreaList.slice(cursor, newCursor),
    };
  },
};
