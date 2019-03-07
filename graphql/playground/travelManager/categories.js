exports.categories = {
  name: 'Travel Manager Category Queries',
  endpoint: 'http://localhost:8080/graphql',
  headers: { sessiontoken: 'advitoValidToken' },
  query: `
  {
    savingsOpportunityDetail(id: 1) {
      id
      metricList {
        title
        personaList {
          title
          value
          hover {
            fields {
              name
              value
            }
            comments
          }
        }
      }
      comments
    }
    riskAreaDetail(id: 1) {
      id
      locationList {
        title
        value
        percent
        latitude
        longitude
        hover {
          fieldList {
            name
            value
          }
          comments
        }
      }
      comments
    }
  }
  `,
};
