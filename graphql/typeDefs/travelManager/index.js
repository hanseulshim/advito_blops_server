const { dashboardDefs, dashboardQueries } = require('./dashboard');
const { savingsOpportunityDefs, savingsOpportunityQueries } = require('./savingsOpportunity');
const { riskAreaDefs, riskAreaQueries } = require('./riskArea');
const { netSpendDefs, netSpendQueries } = require('./netSpend');
const { teBreakdownDefs, teBreakdownQueries } = require('./teBreakdown');

exports.travelManagerDefs = `${dashboardDefs} ${savingsOpportunityDefs} ${riskAreaDefs} ${netSpendDefs} ${teBreakdownDefs}`;
exports.travelManagerQueries = `${dashboardQueries} ${savingsOpportunityQueries} ${riskAreaQueries} ${netSpendQueries} ${teBreakdownQueries}`;
