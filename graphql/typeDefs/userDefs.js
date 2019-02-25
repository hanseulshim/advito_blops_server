const {
  generateType,
  generateTypeList,
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
      nameFirst: String,
      nameLast: String,
      profilePicturePath: String,
      username: String,
      timezoneDefault: String,
      dateFormatDefault: String,
      emailNotifications: Boolean
    }`
  )}

  ${generateTypeList(
    'UserInfo',
    `{
      userId: Int,
      username: String,
      isEnabled: Boolean,
      nameFirst: String,
      nameLast: String,
      phone: String,
      address: String,
      role: String,
      roleId: Int
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
  ${generateQuery('getUsers', 'UserInfo')}
`;

exports.userMutation = `
  updatePassword(clientId: Int!, sessionToken: String!, pwd: String!, confirmPwd: String!): PasswordResponse
  updateUserProfile(
    sessionToken: String!,
    nameFirst: String!,
    nameLast: String!,
    profilePicturePath: String!,
    username: String!,
    dateFormatDefault: String!,
    timezoneDefault: String!,
    emailNotifications: Boolean!
  ): UserProfileResponse
  editUser(userId: Int!,
    sessionToken: String!,
    username: String!,
    isEnabled: Boolean!,
    nameFirst: String!,
    nameLast: String!,
    phone: String,
    address: String,
    roleId: Int,
  ): EditUserResponse
  createUser(clientId: Int!,
    sessionToken: String!,
    username: String!,
    isEnabled: Boolean!,
    nameFirst: String!,
    nameLast: String!,
    phone: String,
    address: String,
    roleId: Int,
    pwd: String!,
    confirmPwd: String!,
  ): CreateUserResponse
`;
