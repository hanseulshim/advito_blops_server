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
const {
  applicationResolvers,
  applicationResolversMutation,
} = require('./applicationResolvers');
const { lambdaInvoke } = require('../helper');

const { portalQueries } = require('./portal');
const { travelManagerQueries } = require('./travelManager');
const { executiveQueries } = require('./executive');
// const { quarterFilterQueries } = require('./quarterFilterResolvers');

exports.resolvers = {
  Query: {
    ...portalQueries,
    ...travelManagerQueries,
    ...executiveQueries,

    ...storyResolvers,
    ...userResolvers,
    ...clientResolvers,
    ...divisionResolvers,
    ...applicationResolvers,
    // ...quarterFilterQueries,
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
    ...applicationResolversMutation
  },
};
