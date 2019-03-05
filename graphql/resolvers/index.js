const { storyResolvers } = require('./storyResolvers');
const { userResolvers, userResolversMutation } = require('./userResolvers');
const {
  clientResolvers,
  clientResolversMutation,
} = require('./clientResolvers');
const {
  divisionResolvers,
  divisionResolversMutation,
} = require('./divisionResolvers');
const { lambdaInvoke } = require('../helper');

const { portalQueries } = require('./portal');
const { travelManagerQueries } = require('./travelManager');
const { executiveQueries } = require('./executive');

exports.resolvers = {
  Query: {
    ...portalQueries,
    ...travelManagerQueries,
    ...executiveQueries,

    ...storyResolvers,
    ...userResolvers,
    ...clientResolvers,
    ...divisionResolvers,
    login: (_, payload) =>
      lambdaInvoke('python-lambdas-dev-user_login', payload),
    logout: (_, payload) => {
      return lambdaInvoke('python-lambdas-dev-user_logout', {
        ...payload,
      });
    },
  },
  Mutation: {
    ...userResolversMutation,
    ...clientResolversMutation,
    ...divisionResolversMutation,
  },
};
