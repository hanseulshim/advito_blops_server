const { generateType } = require('../helper');

exports.userDefs = `
  ${generateType(
    'UserProfile',
    `{
      firstName: String,
      lastName: String,
      profilePicturePath: String,
      username: String,
      timeFormat: String,
      timeZone: String,
      emailNotifications: Boolean
    }`
  )}
`;

exports.userQuery = `
  userProfile(clientId: Int!, sessionToken: String!): UserProfile
`;
