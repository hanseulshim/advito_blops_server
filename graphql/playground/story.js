exports.story = {
  name: 'Story Queries',
  endpoint: 'http://localhost:8080/graphql',
  headers: { sessiontoken: 'advitoValidToken' },
  query: `
  {
    airMap(title: "airSummary") {
      title
      summary
      kpis {
        title
        value
        delta
        percent
        change
        type
        icon
      }
      barchart {
        title
        type
        data {
          category
          value
          change
          delta
          percent
        }
      }
      locations {
        thickness
        height
        opacity
        coords {
          latitude
          longitude
        }
        origin
        destination
      }
    }
    hotelMap(title: "hotelSummary") {
      title
      summary
      kpis {
        title
        value
        delta
        percent
        change
        type
        icon
      }
      barchart {
        title
        type
        data {
          category
          value
          change
          delta
          percent
        }
      }
      locations {
        title
        radius
        latitude
        longitude
      }
    }
    visual(title: "topAirlines") {
      title
      summary
      categories {
        title
        type
        total
        icon
        subCategories {
          name
          value
          delta
          percent
          color
        }
      }
      barchart {
        title
        type
        data {
          category
          change
          value
          delta
          percent
        }
      }
    }
    donut(title: "airRoot") {
      title
      last
      summary
      label
      context
      total
      colors
      donutData {
        category
        value
        nextLevel
        tooltip {
          title
          tooltipData {
            name
            value
          }
        }
      }
    }
  }`,
};
