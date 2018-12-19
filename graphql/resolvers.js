const { activeAlerts, upcomingActions } = require('../data/sidebarData');
const { viewData, infoData } = require('../data/viewData');
const {
  programPerformance,
  noChangeSince,
  personaList,
  opportunities,
  riskAreas,
} = require('../data/dashboardData');

exports.resolvers = {
  Query: {
    activeAlerts: () => activeAlerts,
    upcomingActions: () => upcomingActions,
    infoList: () => infoData,
    viewList: () => viewData,
    performanceList: () => programPerformance,
    noChangeSince: () => noChangeSince,
    personaList: () => personaList,
    opportunities: (parent, args) => opportunities.slice(0, args.limit),
    riskAreas: (parent, args) => riskAreas.slice(0, args.limit),
  },
};
