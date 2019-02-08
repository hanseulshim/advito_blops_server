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
`;

exports.userQuery = `
  ${generateQuery('userProfile', 'UserProfile')}
`;

exports.userMutation = `
  ${generateQuery('updatePassword', 'PasswordResponse')}
`;
