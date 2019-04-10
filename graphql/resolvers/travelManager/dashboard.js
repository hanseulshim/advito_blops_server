const {
  programPerformanceListTravel,
  netSpendAnalysisListTravel,
  personaList,
  savingsOpportunityList,
  riskAreaList,
  noChangeSince,
} = require('../../../data/travelManager/dashboard');

exports.dashboardQueries = {
  programPerformanceListTravel: (_, { filterId }) => {
    if (filterId) {
      return programPerformanceListTravel.map(v => {
        if (v.id === 1) {
          const num = Math.floor(Math.random() * 5000);
          return {
            ...v,
            value: `$${num}`,
          };
        }
        const percent = Math.floor(Math.random() * 50);
        const num = Math.floor(Math.random() * 999);
        return {
          ...v,
          value: `${percent}% / $${num}K`,
        };
      });
    }
    return programPerformanceListTravel;
  },
  netSpendAnalysisListTravel: (_, { filterId }) => {
    if (filterId) {
      return netSpendAnalysisListTravel.map(v => ({
        ...v,
        value: v.value * Math.floor(Math.random() * 15),
      }));
    }
    return netSpendAnalysisListTravel;
  },
  personaList: (_, { filterId }) => {
    if (filterId) {
      return personaList.map(v => ({
        ...v,
        value: `$${Math.floor(Math.random() * 5000)}`,
      }));
    }
    return personaList;
  },
  savingsOpportunityFeedTravel: (
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
          secondaryValue: `$${Math.floor(Math.random() * 900)}K`,
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
  riskAreaFeedTravel: (_, { limit = riskAreaList.length, cursor = 0, filterId }) => {
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
  noChangeSince: (_, { filterId }) => {
    if (filterId) {
      return `July ${Math.floor(Math.random * 30)}`;
    }
    return noChangeSince;
  },
};
