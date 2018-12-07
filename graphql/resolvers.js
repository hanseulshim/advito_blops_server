const { activeAlerts, upcomingActions } = require('../data/sidebarData');
const { viewData, infoData } = require('../data/viewData');
const { programPerformance, noChangeSince } = require('../data/dashboardData');

exports.resolvers = {
  Query: {
    activeAlerts: () => activeAlerts,
    upcomingActions: () => upcomingActions,
    infoList: () => infoData,
    viewList: () => viewData,
    performanceList: () => programPerformance,
    noChangeSince: () => noChangeSince,
  },
};
