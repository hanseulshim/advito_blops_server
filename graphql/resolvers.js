const { activeAlerts, upcomingActions } = require('../data/sidebarData');
const { viewData, infoData } = require('../data/viewData');
const {
  programPerformance,
  noChangeSince,
  personaList,
  opportunities,
  riskAreas,
  logins,
} = require('../data/dashboardData');
//const { logins } = require('../data/loginData');

exports.resolvers = {
  Query: {
    activeAlerts: () => activeAlerts,
    upcomingActions: () => upcomingActions,
    infoList: () => infoData,
    viewList: () => viewData,
    performanceList: () => programPerformance,
    noChangeSince: () => noChangeSince,
    personaList: () => personaList,
    opportunities: (parent, { limit, cursor }) => {
      const totalOpportunities = opportunities.length;
      const newCursor = cursor + limit;
      if (!cursor) {
        cursor = 0;
      }
      const newOpportunities = limit
        ? opportunities.slice(cursor, newCursor)
        : opportunities.slice();
      return {
        cursor: newCursor,
        totalOpportunities,
        hasNext: newCursor < totalOpportunities,
        opportunities: newOpportunities,
      };
    },
    riskAreas: (parent, { limit, cursor }) => {
      const totalRiskAreas = riskAreas.length;
      if (!cursor) {
        cursor = 0;
      }
      const newCursor = cursor + limit;
      const newRiskAreas = limit
        ? riskAreas.slice(cursor, newCursor)
        : riskAreas.slice();
      return {
        cursor: newCursor,
        totalRiskAreas,
        hasNext: newCursor < totalRiskAreas,
        riskAreas: newRiskAreas,
      };
    },
  },
};
