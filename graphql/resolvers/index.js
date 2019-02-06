const { consoleResolvers } = require('./consoleResolvers');
const { storyResolvers } = require('./storyResolvers');
const { generateResponse, lambdaInvoke } = require('../helper');

exports.resolvers = {
  Query: {
    ...consoleResolvers,
    ...storyResolvers,
    login: (_, payload) => {
      return lambdaInvoke('python-lambdas-dev-user_login', {
        username: payload.username,
        pwd: payload.pwd,
      });
    },
  },
};
