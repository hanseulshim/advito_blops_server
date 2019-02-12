const { activeAlerts, upcomingActions } = require('../../data/sidebarData');
const { viewData, infoData } = require('../../data/viewData');
const {
  programPerformanceTravel,
  programPerformanceExecutive,
  netSpendAnalysisTravel,
  netSpendAnalysisExecutive,
  noChangeSince,
  personaList,
  marketList,
  opportunitiesTravel,
  opportunitiesExecutive,
  riskAreasTravel,
  riskAreasExecutive,
} = require('../../data/dashboardData');

const { lambdaFakeInvoke } = require('../helper');

exports.consoleResolvers = {
  activeAlerts: (_, payload) => lambdaFakeInvoke(payload, activeAlerts),
  upcomingActions: (_, payload) => lambdaFakeInvoke(payload, upcomingActions),
  infoData: (_, payload) => lambdaFakeInvoke(payload, infoData),
  viewData: (_, payload) => lambdaFakeInvoke(payload, viewData),
  programPerformanceTravel: (_, payload) =>
    lambdaFakeInvoke(payload, programPerformanceTravel),
  programPerformanceExecutive: (_, payload) =>
    lambdaFakeInvoke(payload, programPerformanceExecutive),
  netSpendAnalysisTravel: (_, payload) =>
    lambdaFakeInvoke(payload, netSpendAnalysisTravel),
  netSpendAnalysisExecutive: (_, payload) =>
    lambdaFakeInvoke(payload, netSpendAnalysisExecutive),
  noChangeSince: (_, payload) => lambdaFakeInvoke(payload, noChangeSince),
  personaList: (_, payload) => lambdaFakeInvoke(payload, personaList),
  marketList: (_, payload) => lambdaFakeInvoke(payload, marketList),
  opportunitiesTravel: (
    _,
    { limit = opportunitiesTravel.length, cursor = 0, ...payload }
  ) => {
    const totalOpportunities = opportunitiesTravel.length;
    const newCursor = cursor + limit;
    const prevCursor = cursor - limit < 0 ? 0 : cursor - limit;
    return lambdaFakeInvoke(payload, {
      prevCursor,
      cursor: newCursor,
      totalOpportunities,
      hasNext: newCursor < totalOpportunities,
      opportunities: opportunitiesTravel.slice(cursor, newCursor),
    });
  },
  opportunitiesExecutive: (
    _,
    { limit = opportunitiesExecutive.length, cursor = 0, ...payload }
  ) => {
    const totalOpportunities = opportunitiesExecutive.length;
    const newCursor = cursor + limit;
    const prevCursor = cursor - limit < 0 ? 0 : cursor - limit;
    return lambdaFakeInvoke(payload, {
      prevCursor,
      cursor: newCursor,
      totalOpportunities,
      hasNext: newCursor < totalOpportunities,
      opportunities: opportunitiesExecutive.slice(cursor, newCursor),
    });
  },
  riskAreasTravel: (
    _,
    { limit = riskAreasTravel.length, cursor = 0, ...payload }
  ) => {
    const totalRiskAreas = riskAreasTravel.length;
    const newCursor = cursor + limit;
    const prevCursor = cursor - limit < 0 ? 0 : cursor - limit;
    return lambdaFakeInvoke(payload, {
      prevCursor: prevCursor,
      cursor: newCursor,
      totalRiskAreas,
      hasNext: newCursor < totalRiskAreas,
      riskAreas: riskAreasTravel.slice(cursor, newCursor),
    });
  },
  riskAreasExecutive: (
    _,
    { limit = riskAreasExecutive.length, cursor = 0, ...payload }
  ) => {
    const totalRiskAreas = riskAreasExecutive.length;
    const newCursor = cursor + limit;
    const prevCursor = cursor - limit < 0 ? 0 : cursor - limit;
    return lambdaFakeInvoke(payload, {
      prevCursor: prevCursor,
      cursor: newCursor,
      totalRiskAreas,
      hasNext: newCursor < totalRiskAreas,
      riskAreas: riskAreasExecutive.slice(cursor, newCursor),
    });
  },
};
