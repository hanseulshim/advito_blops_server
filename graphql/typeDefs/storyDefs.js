exports.storyDefs = `
  type ArcMap {
    thickness: Float,
    height: Float,
    opacity: Float,
    coords: [Coordinate],
    from: String,
    to: String,
  }

  type Bar {
    category: String,
    value: Float,
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
    change: String,
    type: String,
    icon: String,
  }

  type Visualization {
    title: String,
    icon: String,
    total: Float,
    subCategories: [VisualizationCategory]
  }

  type VisualizationCategory {
    name: String,
    value: Float,
    delta: Float,
    color: String,
  }

  type AirMap {
    title: String
    summary: String
    kpis: [Kpi]
    barchart: [Barchart]
    locations: [ArcMap]
  }

  type AirPlane {
    title: String
    summary: String
    categories: [Visualization]
    barchart: [Barchart]
  }
`;

exports.storyQuery = `
  airMap(title: String!): AirMap
  airPlane(title: String!): AirPlane
`;
