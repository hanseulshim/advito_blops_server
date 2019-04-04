exports.riskAreaDefs = `
type RiskAreaDetail {
  id: Int
  locationList: [RiskAreaLocation]
  comments: [String]
}

type RiskAreaLocation {
  title: String
  percent: Float
  value: Float
  latitude: Float
  longitude: Float
  hover: RiskAreaHover
}

type RiskAreaHover {
  fieldList: [RiskAreaField]
  comments: [String]
}

type RiskAreaField {
  name: String,
  value: String
}
`;

exports.riskAreaQueries = `
  riskAreaDetail(id: Int!, filterId: Int): RiskAreaDetail @auth
`;
