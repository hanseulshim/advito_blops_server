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

  type AirMap {
    title: String
    summary: String
    kpis: [Kpi]
    barchart: [Barchart]
    locations: [ArcMap]
  }

  type HotelMap {
    title: String
    summary: String
    kpis: [Kpi]
    barchart: [Barchart]
    locations: [PointMap]
  }

  type Visual {
    title: String
    summary: String
    categories: [Visualization]
    barchart: [Barchart]
  }

  type DonutList {
    title: String,
    last: Boolean,
    summary: String,
    label: String,
    context: String,
    total: Float,
    colors: [String]
    donutData: [Donut]
  }
`;

exports.storyQuery = `
  airMap(title: String!): AirMap @auth
  hotelMap(title: String!): HotelMap @auth
  visual(title: String!): Visual @auth
  donut(title: String!): DonutList @auth
`;
