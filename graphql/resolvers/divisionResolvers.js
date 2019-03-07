const { lambdaInvoke } = require('../helper');

exports.divisionResolvers = {
  divisionList: (_, payload, { sessionToken }) =>
    lambdaInvoke('python-lambdas-dev-client_division_get_all', {
      ...payload,
      sessionToken,
    }),
};

exports.divisionResolversMutation = {
  updateDivision: async (_, payload, { sessionToken }) => {
    await lambdaInvoke('python-lambdas-dev-client_division_update', {
      ...payload,
      sessionToken,
    });
    return payload;
  },
  createDivision: (_, payload, { sessionToken }) =>
    lambdaInvoke('python-lambdas-dev-client_division_create', {
      ...payload,
      sessionToken,
    }),
};
