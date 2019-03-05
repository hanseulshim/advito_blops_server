exports.login = {
  name: 'Login Queries',
  endpoint: 'http://localhost:8080/graphql',
  headers: { sessiontoken: 'advitoValidToken' },
  query: `
  {
    login(username:"hshim@boostlabs.com", pwd:"Password2") {
      displayName
      clientId
      profilePicturePath
      sessionToken
    }
  }`,
};
