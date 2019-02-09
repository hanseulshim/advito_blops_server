const { generateType } = require('../helper');

exports.storyDefs = `
  type ArcMap {
    thickness: Float,
    height: Float,
    opacity: Float,
    coords: [Coordinate],
    origin: String,
    destination: String,
  }

  type Bar {
    category: String,
    value: Float,
    delta: Float,
    percent: Float,
    change: String,
  }

  type Barchart {
    title: String,
    type: String,
    data: [Bar],
  }

  type Coordinate {
    latitude: Float,
    longitude: Float,
  }

  type Kpi {
    title: String,
    value: Float,
    delta: Float,
    percent: Float,
    change: String,
    type: String,
    icon: String,
  }

  type PointMap {
    title: String,
    radius: Int,
    latitude: Float,
    longitude: Float,
  }

  type Visualization {
    title: String,
    type: String,
    icon: String,
    total: Float,
    subCategories: [VisualizationCategory]
  }

  type VisualizationCategory {
    name: String,
    value: Float,
    delta: Float,
    percent: Float,
    color: String,
  }

  type TooltipData {
    value: Float,
    name: String,
  }

  type Tooltip {
    title: String,
    tooltipData: [TooltipData]
  }

  type Donut {
    category: String,
    value: Float,
    nextLevel: String,
    tooltip: Tooltip
  }

  ${generateType(
    'AirMap',
    `{
      title: String
      summary: String
      kpis: [Kpi]
      barchart: [Barchart]
      locations: [ArcMap]
    }`
  )}

  ${generateType(
    'HotelMap',
    `{
      title: String
      summary: String
      kpis: [Kpi]
      barchart: [Barchart]
      locations: [PointMap]
    }`
  )}

  ${generateType(
    'Visual',
    `{
      title: String
      summary: String
      categories: [Visualization]
      barchart: [Barchart]
    }`
  )}

  ${generateType(
    'DonutList',
    `{
      title: String,
      last: Boolean,
      summary: String,
      label: String,
      context: String,
      total: Float,
      colors: [String]
      donutData: [Donut]
    }`
  )}
`;

exports.storyQuery = `
  airMap(clientId: Int!, sessionToken: String!, title: String!): AirMap
  hotelMap(clientId: Int!, sessionToken: String!, title: String!): HotelMap
  visual(clientId: Int!, sessionToken: String!, title: String!): Visual
  donut(clientId: Int!, sessionToken: String!, title: String!): DonutList
`;
