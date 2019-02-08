const { generateType } = require('../helper');

exports.loginDefs = `
${generateType(
  'Login',
  `{
  displayName: String,
  clientId: Int,
  profilePicturePath: String,
  sessionToken: String,
}`
)}

type LogoutBody {
  success: Boolean,
  apicode: String,
  apimessage: String,
  apidataset: String,
}

type Logout {
  statusCode: Int,
  body: LogoutBody
}

`;

exports.loginQuery = `
  login(username: String!, pwd: String!): Login
  logout(sessionToken: String!): Logout
`;
