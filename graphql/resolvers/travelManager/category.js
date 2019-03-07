const {
  savingsOpportunities,
} = require('../../../data/travelManager/savingsOpportunity');
const { riskAreas } = require('../../../data/travelManager/riskArea');

exports.categoryQueries = {
  savingsOpportunityDetail: (_, payload) =>
    savingsOpportunities[payload.id - 1],
  riskAreaDetail: (_, payload) => riskAreas[payload.id - 1],
};
