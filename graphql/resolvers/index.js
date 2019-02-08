const { consoleResolvers } = require('./consoleResolvers');
const { storyResolvers } = require('./storyResolvers');
const { userResolvers } = require('./userResolvers');
const { generateResponse, lambdaInvoke } = require('../helper');

exports.resolvers = {
  Query: {
    ...consoleResolvers,
    ...storyResolvers,
    ...userResolvers,
    login: (_, payload) => {
      return lambdaInvoke('python-lambdas-dev-user_login', {
        username: payload.username,
        pwd: payload.pwd,
      });
    },
    logout: (_, payload) => {
      return lambdaInvoke('python-lambdas-dev-user_logout', {
        ...payload,
      });
    },
  },
};
