const { lambdaInvoke } = require('../helper');

exports.divisionResolvers = {
  getDivisions: (_, payload) =>
    lambdaInvoke('python-lambdas-dev-client_division_get_all', {
      ...payload,
    }),
};

exports.divisionResolversMutation = {
  updateDivision: (_, payload) =>
    lambdaInvoke('python-lambdas-dev-client_division_update', { ...payload }),
  createDivision: (_, payload) =>
    lambdaInvoke('python-lambdas-dev-client_division_create', { ...payload }),
};