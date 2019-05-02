exports.userDefs = `
  type UserProfile {
    nameFirst: String,
    nameLast: String,
    profilePicturePath: String,
    username: String,
    timezoneDefault: String,
    dateFormatDefault: String,
    emailNotifications: Boolean
  }

  type UserProfileOverview {
    myApplications: [String]
    persona: String
    recentActivities: [RecentActivity]
  }

  type RecentActivity {
    date: String,
    activity: String,
  }

  type UserInfo {
    id: Int,
    username: String,
    isEnabled: Boolean,
    nameFirst: String,
    nameLast: String,
    phone: String,
    address: String,
    role: String,
    roleId: Int
  }
`;

exports.userQuery = `
  userProfile: UserProfile @auth
  userProfileOverview: UserProfileOverview @auth
  userList(clientId: Int): [UserInfo] @auth
`;

exports.userMutation = `
  updatePassword(pwd: String!, confirmPwd: String!): String @auth
  updateUserProfile(
    nameFirst: String!,
    nameLast: String!,
    profilePicturePath: String!,
    username: String!,
    dateFormatDefault: String!,
    timezoneDefault: String!,
    emailNotifications: Boolean!
  ): String @auth
  editUser(id: Int!,
    username: String!,
    isEnabled: Boolean!,
    nameFirst: String!,
    nameLast: String!,
    phone: String,
    address: String,
    roleId: Int,
  ): UserInfo @auth
  createUser(
    clientId: Int!
    username: String!,
    isEnabled: Boolean!,
    nameFirst: String!,
    nameLast: String!,
    phone: String,
    address: String,
    roleId: Int,
    pwd: String!,
    confirmPwd: String!,
  ): UserInfo @auth
`;
