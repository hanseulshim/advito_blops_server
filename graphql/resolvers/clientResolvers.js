const { lambdaInvoke } = require('../helper');

exports.clientResolvers = {
  clientList: (_, payload, { sessionToken }) =>
    lambdaInvoke('python-lambdas-dev-client_get_all', {
      ...payload,
      sessionToken,
    }),
  }
  
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