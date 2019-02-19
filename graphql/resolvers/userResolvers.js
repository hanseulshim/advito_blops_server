const { lambdaInvoke, lambdaFakeInvoke } = require('../helper');
const { userProfileOverview } = require('../../data/userProfileData');
exports.userResolvers = {
  userProfile: (_, payload) =>
    lambdaInvoke('python-lambdas-dev-user_get', {
      ...payload,
    }),
  getUsers: (_, payload) =>
    lambdaInvoke('python-lambdas-dev-user_access', {
      ...payload,
    }),
  userProfileOverview: (_, payload) =>
    lambdaFakeInvoke(payload, userProfileOverview),
};

exports.userResolversMutation = {
  updatePassword: (_, payload) => lambdaFakeInvoke(payload),
  updateUserProfile: (_, payload) =>
    lambdaInvoke('python-lambdas-dev-user_update', { ...payload }),
  createUser: (_, payload) =>
    lambdaInvoke('python-lambdas-dev-user_create', { ...payload }),
  editUser: (_, payload) =>
    lambdaInvoke('python-lambdas-dev-user_update_any', { ...payload }),
};
