const { lambdaInvoke } = require('../helper');
const { userProfileOverview } = require('../../data/userProfileData');
exports.userResolvers = {
  userProfile: (_, __, { sessionToken }) =>
    lambdaInvoke('python-lambdas-dev-user_get', {
      sessionToken,
    }),
  userList: (_, __, { sessionToken }) =>
    lambdaInvoke('python-lambdas-dev-user_access', {
      sessionToken,
    }),
  userProfileOverview: () => userProfileOverview,
};

exports.userResolversMutation = {
  updatePassword: () => 'Password Updated',
  updateUserProfile: (_, payload, { sessionToken }) =>
    lambdaInvoke('python-lambdas-dev-user_update', {
      ...payload,
      sessionToken,
    }),
  createUser: (_, payload, { sessionToken }) =>
    lambdaInvoke('python-lambdas-dev-user_create', {
      ...payload,
      sessionToken,
    }),
  editUser: async (_, payload, { sessionToken }) => {
    await lambdaInvoke('python-lambdas-dev-user_update_any', {
      ...payload,
      sessionToken,
    });
    return payload
  }

};
