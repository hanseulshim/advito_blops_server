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

  type Donut {
    category: String,
    value: Float,
    nextLevel: String,
  }

  type DonutList {
    title: String,
    summary: String,
    label: String,
    context: String,
    total: Float,
    colors: [String]
    donutData: [Donut]
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
`;

exports.storyQuery = `
  airMap(title: String!): AirMap
  hotelMap(title: String!): HotelMap
  visual(title: String!): Visual
  donut(title: String!): DonutList
`;
