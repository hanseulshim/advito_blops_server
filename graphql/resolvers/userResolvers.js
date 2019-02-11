const { lambdaFakeInvoke } = require('../helper');
const {
  userProfile,
  userProfileOverview,
} = require('../../data/userProfileData');
exports.userResolvers = {
  userProfile: (_, payload) => lambdaFakeInvoke(payload, userProfile),
  userProfileOverview: (_, payload) =>
    lambdaFakeInvoke(payload, userProfileOverview),
};

exports.userResolversMutation = {
  updatePassword: (_, payload) => lambdaFakeInvoke(payload),
  updateUserProfile: (_, payload) => lambdaFakeInvoke(payload),
};
