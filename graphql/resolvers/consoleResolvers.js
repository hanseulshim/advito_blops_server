const { activeAlerts, upcomingActions } = require('../../data/sidebarData');
const { viewData, infoData } = require('../../data/viewData');
const {
  programPerformance,
  noChangeSince,
  personaList,
  marketList,
  opportunities,
  riskAreas,
} = require('../../data/dashboardData');

const { lambdaFakeInvoke } = require('../helper');

exports.consoleResolvers = {
  activeAlerts: (_, payload) => lambdaFakeInvoke(payload, activeAlerts),
  upcomingActions: (_, payload) => lambdaFakeInvoke(payload, upcomingActions),
  infoData: (_, payload) => lambdaFakeInvoke(payload, infoData),
  viewData: (_, payload) => lambdaFakeInvoke(payload, viewData),
  programPerformance: (_, payload) =>
    lambdaFakeInvoke(payload, programPerformance),
  noChangeSince: (_, payload) => lambdaFakeInvoke(payload, noChangeSince),
  personaList: (_, payload) => lambdaFakeInvoke(payload, personaList),
  marketList: (_, payload) => lambdaFakeInvoke(payload, marketList),
  opportunities: (
    _,
    { limit = opportunities.length, cursor = 0, ...payload }
  ) => {
    const totalOpportunities = opportunities.length;
    const newCursor = cursor + limit;
    const prevCursor = cursor - limit < 0 ? 0 : cursor - limit;
    return lambdaFakeInvoke(payload, {
      prevCursor,
      cursor: newCursor,
      totalOpportunities,
      hasNext: newCursor < totalOpportunities,
      opportunities: opportunities.slice(cursor, newCursor),
    });
  },
  riskAreas: (_, { limit = riskAreas.length, cursor = 0, ...payload }) => {
    const totalRiskAreas = riskAreas.length;
    const newCursor = cursor + limit;
    const prevCursor = cursor - limit < 0 ? 0 : cursor - limit;
    return lambdaFakeInvoke(payload, {
      prevCursor: prevCursor,
      cursor: newCursor,
      totalRiskAreas,
      hasNext: newCursor < totalRiskAreas,
      riskAreas: riskAreas.slice(cursor, newCursor),
    });
  },
};
