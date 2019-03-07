exports.userQueries = {
  name: 'User Queries',
  endpoint: 'http://localhost:8080/graphql',
  headers: { sessiontoken: 'advitoValidToken' },
  query: `
  {
    userProfile {
      nameFirst
      nameLast
      profilePicturePath
      username
      timezoneDefault
      dateFormatDefault
      emailNotifications
    }
    userProfileOverview {
      myApplications
      persona
      recentActivities {
        date
        activity
      }
    }
    userList {
      id
      username
      isEnabled
      nameFirst
      nameLast
      phone
      address
      role
      roleId
    }
  }`,
};

exports.userMutations = {
  name: 'User Mutations',
  endpoint: 'http://localhost:8080/graphql',
  headers: { sessiontoken: 'advitoValidToken' },
  query: `
  mutation {
    updatePassword(pwd: "Password2", confirmPwd: "Password2")
    updateUserProfile(
      nameFirst: "hanseul",
      nameLast: "shim",
      profilePicturePath: "test",
      username: "hshim@boostlabs.com",
      dateFormatDefault: "test",
      timezoneDefault: "test",
      emailNotifications: false,
    )
    editUser(
      id: 765,
      username: "admin@boostlabs.com",
      isEnabled: true,
      nameFirst: "First name",
      nameLast: "last name",
      phone: "phone",
      address: "address",
      roleId: 1,
    ) {
      id
      username
      isEnabled
      nameFirst
      nameLast
      phone
      address
      roleId
    }
    createUser(
      clientId: 1,
      username: "testuser@advito.com",
      isEnabled: true,
      nameFirst: "first test",
      nameLast: "last test",
      phone: "13123123123",
      address: "123 fake street",
      roleId: 1,
      pwd: "Password2",
      confirmPwd: "Password2",
    )
  }`,
};
