exports.divisionQueries = {
  name: 'Division Queries',
  endpoint: 'http://localhost:8080/graphql',
  headers: { sessiontoken: 'advitoValidToken' },
  query: `
  {
    divisionList(clientId: 1) {
      id
      clientId
      divisionName
      divisionNameFull
      divisionTag
      gcn
      isActive
      description
    }
  }`,
};

exports.divisionMutations = {
  name: 'Division Mutations',
  endpoint: 'http://localhost:8080/graphql',
  headers: { sessiontoken: 'advitoValidToken' },
  query: `
  mutation {
    updateDivision(
      clientDivisionId: 1,
      divisionName: "division name",
      divisionNameFull: "divisionn",
      isActive: true,
      divisionTag: "tag",
      gcn: "gcn",
      description: "description"
    )
    createDivision(
      clientId: 1,
      divisionName: "division name",
      divisionNameFull: "divisionn",
      isActive: true,
      divisionTag: "tag",
      gcn: "gcn",
      description: "description"
    )
  }`,
};
