const { lambdaFakeInvoke } = require('../helper')
const { riskAreaDetailData } = require('../../data/riskAreaDetailData')
exports.riskAreaDetailResolvers = {
  riskAreaDetail: (_, payload) =>
    lambdaFakeInvoke(payload, riskAreaDetailData[payload.id - 1]),
}
