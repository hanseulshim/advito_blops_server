exports.quarterFilter = {
  name: 'Quarter Filter Queries',
  endpoint: 'http://localhost:8080/graphql',
  headers: { sessiontoken: 'advitoValidToken' },
  query: `
  {
    quarterFilterList {
      id
      value
    }
  }`,
};
