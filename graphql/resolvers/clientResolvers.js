const { lambdaInvoke } = require('../helper');

exports.clientResolvers = {
  clientList: async (_, payload, { sessionToken }) => {
    const result = await lambdaInvoke('python-lambdas-dev-client_get_all', {
      ...payload,
      sessionToken,
    });
    console.log(result);
    return result;
  }
};

exports.clientResolversMutation = {
  updateClient: (_, payload, { sessionToken }) =>
    lambdaInvoke('python-lambdas-dev-client_update', {
      ...payload,
      sessionToken,
    }),
  createClient: (_, payload, { sessionToken }) =>
    lambdaInvoke('python-lambdas-dev-client_create', {
      ...payload,
      sessionToken,
    }),
};