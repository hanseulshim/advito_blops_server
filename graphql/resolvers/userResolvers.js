const { lambdaFakeInvoke } = require('../helper');
const { userProfile } = require('../../data/userProfileData');
exports.userResolvers = {
  userProfile: (_, payload) => lambdaFakeInvoke(payload, userProfile),
};
