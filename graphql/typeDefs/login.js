exports.loginDefs = `
type Login {
  displayName: String,
  clientId: Int,
  profilePicturePath: String,
  sessionToken: String,
}

`;

exports.loginQuery = `
  login(username: String!, pwd: String!): Login
  logout(sessionToken: String!): String @auth
`;
