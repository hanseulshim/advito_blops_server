const { lambdaInvoke } = require('../helper');

exports.clientResolvers = {
  getClients: (_, payload) =>
    lambdaInvoke('python-lambdas-dev-client_get_all', {
      ...payload,
    }),
};

exports.clientResolversMutation = {
  updateClient: (_, payload) =>
    lambdaInvoke('python-lambdas-dev-client_update', { ...payload }),
  createClient: (_, payload) =>
    lambdaInvoke('python-lambdas-dev-client_create', { ...payload }),
};