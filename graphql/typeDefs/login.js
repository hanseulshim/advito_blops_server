exports.loginDefs = `
type Login {
  displayName: String,
  clientId: Int,
  profilePicturePath: String,
  sessionToken: String,
  roleIds: [Int]
}

`;

exports.loginQuery = `
  login(username: String!, pwd: String!): Login
  logout(sessionToken: String!): String @auth
`;
