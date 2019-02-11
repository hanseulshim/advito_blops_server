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
  ${generateMutationType('CreateUserResponse')}
  ${generateMutationType('EditUserResponse')}
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
  editUser(clientId: Int!,
    sessionToken: String!,
    username: String!,
    accountActive: Boolean!,
    firstName: String!,
    lastName: String!,
    phone: String,
    address: String,
    role: String,
    pwd: String
  ): EditUserResponse
  createUser(clientId: Int!,
    sessionToken: String!,
    username: String!,
    accountActive: Boolean!,
    firstName: String!,
    lastName: String!,
    phone: String,
    address: String,
    role: String,
    pwd: String!
  ): CreateUserResponse
`;
