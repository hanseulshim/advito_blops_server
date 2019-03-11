exports.applicationQueries = {
  name: 'Application Queries',
  endpoint: 'http://localhost:8080/graphql',
  headers: { sessiontoken: 'advitoValidToken' },
  query: `
  {
    noClient: applicationList {
      id
      applicationName
      applicationFull
      applicationTag
      isActive
      description
      features {
        id
        featureName
        featureTag
        isActive
        description
      }
    }
    client: applicationList(clientId: 1) {
      id
      applicationName
      applicationFull
      applicationTag
      isActive
      description
      features {
        id
        featureName
        featureTag
        isActive
        description
      }
    }
  }`,
};

exports.applicationMutations = {
  name: 'Application Mutations',
  endpoint: 'http://localhost:8080/graphql',
  headers: { sessiontoken: 'advitoValidToken' },
  query: `
  mutation {
    setFeatures(
      clientId: 26,
      featureIds: [1, 3]
    )
  }`,
};
