const { activeAlerts, upcomingActions } = require('../data/sidebarData');
const { viewData, infoData } = require('../data/viewData');

exports.resolvers = {
  Query: {
    scott: () => 'boss',
    john: () => 'lil johnny!',
    shayan: () => 'call linda asap!',
    hanseul: () => 'han solo!',
    activeAlerts: () => activeAlerts,
    upcomingActions: () => upcomingActions,
    infoList: () => infoData,
    viewList: () => viewData,
  },
};
