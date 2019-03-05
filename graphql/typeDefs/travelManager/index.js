const { dashboardDefs, dashboardQueries } = require('./dashboard');
const {
  savingsOpportunityDefs,
  savingsOpportunityQueries,
} = require('./savingsOpportunity');
const { riskAreaDefs, riskAreaQueries } = require('./riskArea');

exports.travelManagerDefs = `${dashboardDefs} ${savingsOpportunityDefs} ${riskAreaDefs}`;
exports.travelManagerQueries = `${dashboardQueries} ${savingsOpportunityQueries} ${riskAreaQueries}`;
