exports.clientQueries = {
  name: 'Client Queries',
  endpoint: 'http://localhost:8080/graphql',
  headers: { sessiontoken: 'advitoValidToken' },
  query: `
  {
    clientList {
      id
      clientName
      clientNameFull
      clientTag
      gcn
      lanyonClientCode
      isActive
      industry
      defaultCurrencyCode
      defaultDistanceUnits
      description
    }
  }`,
};

exports.clientMutations = {
  name: 'Client Mutations',
  endpoint: 'http://localhost:8080/graphql',
  headers: { sessiontoken: 'advitoValidToken' },
  query: `
  mutation {
    updateClient(
      clientId: 2,
      clientName: "Pepco",
      clientNameFull: "Pepco Inc.",
      clientTag: "",
      gcn: "",
      lanyonClientCode: "",
      isActive: true,
      logoPath: "",
      industry: "Public Service",
      defaultCurrencyCode: "Dollar",
      defaultDistanceUnits: "Kilometers",
      description: ""
    )
    createClient(
      clientName: "test company",
      clientNameFull: "test",
      clientTag: "tag",
      gcn: "123",
      lanyonClientCode: "123",
      isActive: true,
      logoPath: "none",
      industry: "Tech",
      defaultCurrencyCode: "USD",
      defaultDistanceUnits: "miles",
      description: "Im a company"
    )
  }`,
};
