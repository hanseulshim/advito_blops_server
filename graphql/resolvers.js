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
    opportunities: () => opportunities,
    riskAreas: () => riskAreas,
    logins: (username, password) => { console.log(username); return logins },
  },
};
