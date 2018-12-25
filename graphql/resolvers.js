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
    opportunities: (parent, { limit = opportunities.length, cursor = 0 }) => {
      const totalOpportunities = opportunities.length;
      const newCursor = cursor + limit;
      return {
        cursor: newCursor,
        totalOpportunities,
        hasNext: newCursor < totalOpportunities,
        opportunities: opportunities.slice(cursor, newCursor),
      };
    },
    riskAreas: (parent, { limit = riskAreas.length, cursor = 0 }) => {
      const totalRiskAreas = riskAreas.length;
      const newCursor = cursor + limit;
      return {
        cursor: newCursor,
        totalRiskAreas,
        hasNext: newCursor < totalRiskAreas,
        riskAreas: riskAreas.slice(cursor, newCursor),
      };
    },
  },
};
