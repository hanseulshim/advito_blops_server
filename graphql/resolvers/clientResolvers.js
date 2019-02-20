const { lambdaInvoke } = require('../helper');

exports.clientResolvers = {
  getClients: (_, payload) =>
    lambdaInvoke('python-lambdas-dev-client_get_all', {
      ...payload,
    }),
}