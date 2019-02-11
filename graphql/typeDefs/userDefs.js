const {
  generateType,
  generateQuery,
  generateMutationType,
} = require('../helper');

exports.userDefs = `
  type RecentActivity {
    date: String,
    activity: String,
  }

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

  ${generateType(
    'UserProfileOverview',
    `{
      myApplications: [String]
      persona: String
      recentActivities: [RecentActivity]
    }`
  )}

  ${generateMutationType('PasswordResponse')}
  ${generateMutationType('UserProfileResponse')}
`;

exports.userQuery = `
  ${generateQuery('userProfile', 'UserProfile')}
  ${generateQuery('userProfileOverview', 'UserProfileOverview')}
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
