const { lambdaFakeInvoke } = require('../helper')
const {
  savingsOpportunityDetailData,
} = require('../../data/savingsOpportunityDetailData')
exports.savingsOpportunityDetailResolvers = {
  savingsOpportunityDetail: (_, payload) =>
    lambdaFakeInvoke(payload, savingsOpportunityDetailData[payload.id - 1]),
}
