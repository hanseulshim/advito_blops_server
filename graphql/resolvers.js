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
      let newOpportunities = [];
      if (!cursor) {
        cursor = 0;
      }
      if (!limit) {
        newOpportunities = opportunities.slice();
      }
      newOpportunities = opportunities.slice(cursor, newCursor);
      return {
        cursor: newCursor,
        totalOpportunities,
        hasNext: newCursor < totalOpportunities,
        opportunities: newOpportunities,
      };
    },
    riskAreas: (parent, { limit, cursor }) => {
      const totalRiskAreas = riskAreas.length;
      const newCursor = cursor + limit;
      let newRiskAreas = [];
      if (!cursor) {
        cursor = 0;
      }
      if (!limit) {
        newRiskAreas = riskAreas.slice();
      }
      newRiskAreas = riskAreas.slice(cursor, newCursor);
      return {
        cursor: newCursor,
        totalRiskAreas,
        hasNext: newCursor < totalRiskAreas,
        riskAreas: newRiskAreas,
      };
    },
  },
};
