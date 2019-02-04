const { activeAlerts, upcomingActions } = require('../../data/sidebarData');
const { viewData, infoData } = require('../../data/viewData');
const {
  programPerformance,
  noChangeSince,
  personaList,
  opportunities,
  riskAreas,
} = require('../../data/dashboardData');

const { generateResponse } = require('../helper');

exports.consoleResolvers = {
  activeAlerts: () => generateResponse(activeAlerts),
  upcomingActions: () => generateResponse(upcomingActions),
  infoData: () => generateResponse(infoData),
  viewData: () => generateResponse(viewData),
  programPerformance: () => generateResponse(programPerformance),
  noChangeSince: () => generateResponse(noChangeSince),
  personaList: () => generateResponse(personaList),
  opportunities: (parent, { limit = opportunities.length, cursor = 0 }) => {
    const totalOpportunities = opportunities.length;
    const newCursor = cursor + limit;
    const prevCursor = cursor - limit < 0 ? 0 : cursor - limit;
    return generateResponse({
      prevCursor,
      cursor: newCursor,
      totalOpportunities,
      hasNext: newCursor < totalOpportunities,
      opportunities: opportunities.slice(cursor, newCursor),
    });
  },
  riskAreas: (parent, { limit = riskAreas.length, cursor = 0 }) => {
    const totalRiskAreas = riskAreas.length;
    const newCursor = cursor + limit;
    const prevCursor = cursor - limit < 0 ? 0 : cursor - limit;
    return generateResponse({
      prevCursor: prevCursor,
      cursor: newCursor,
      totalRiskAreas,
      hasNext: newCursor < totalRiskAreas,
      riskAreas: riskAreas.slice(cursor, newCursor),
    });
  },
};
