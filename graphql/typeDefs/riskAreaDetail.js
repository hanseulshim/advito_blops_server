const { generateType } = require('../helper')

exports.riskAreaDefs = `
${generateType(
  'RiskAreaDetail',
  `{
    id: Int
    locationList: [RiskAreaLocation]
    comments: [String],
}`,
)}

type RiskAreaLocation {
  title: String
  percent: Float
  value: Float
  latitude: Float
  longitude: Float
  hover: RiskAreaHover
}

type RiskAreaHover {
  fields: [RiskAreaField]
  comments: [String]
}

type RiskAreaField {
  name: String,
  value: String
}
`

exports.riskAreaQuery = `
  riskAreaDetail(sessionToken: String!, id: Int!): RiskAreaDetail
`
