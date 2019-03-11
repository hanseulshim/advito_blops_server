const { lambdaInvoke } = require('../helper');

exports.applicationResolvers = {
  applicationList: (_, payload, { sessionToken }) =>
    lambdaInvoke('python-lambdas-dev-application_get', {
      ...payload,
      sessionToken,
    }),
};

exports.applicationResolversMutation = {
  setFeatures: async (_, payload, { sessionToken }) => {
    await lambdaInvoke('python-lambdas-dev-client_set_features', {
      ...payload,
      sessionToken,
    });
    return payload.featureIds;
  },
};
