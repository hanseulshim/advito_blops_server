const { dashboardDefs, dashboardQueries } = require('./dashboard');
const { savingsOpportunityDefs, savingsOpportunityQueries } = require('./savingsOpportunity');
const { riskAreaDefs, riskAreaQueries } = require('./riskArea');
const { netSpendDefs, netSpendQueries } = require('./netSpend');

exports.travelManagerDefs = `${dashboardDefs} ${savingsOpportunityDefs} ${riskAreaDefs} ${netSpendDefs}`;
exports.travelManagerQueries = `${dashboardQueries} ${savingsOpportunityQueries} ${riskAreaQueries} ${netSpendQueries}`;
