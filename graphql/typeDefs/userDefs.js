const {
  generateType,
  generateQuery,
  generateMutationType,
} = require('../helper');

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

  ${generateMutationType('PasswordResponse')}
  ${generateMutationType('UserProfileResponse')}
`;

exports.userQuery = `
  ${generateQuery('userProfile', 'UserProfile')}
`;

exports.userMutation = `
  updatePassword(clientId: Int!, sessionToken: String!, pwd: String!): PasswordResponse
  updateUserProfile(clientId: Int!,
    sessionToken: String!,
    firstName: String!,
    lastName: String!,
    profilePicturePath: String!,
    username: String!,
    timeFormat: String!,
    timeZone: String!,
    emailNotifications: Boolean!
  ): UserProfileResponse
`;
