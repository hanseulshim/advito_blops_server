const { generateType } = require('../helper');

exports.loginDefs = generateType(
  'Login',
  `{
  displayName: String,
  clientId: Int,
  profilePicturePath: String,
  sessionToken: String,
}`
);

exports.loginQuery = `
  login(username: String, password: String): Login
`;
