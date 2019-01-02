const { consoleResolvers } = require('./consoleResolvers');
const { storyResolvers } = require('./storyResolvers');

exports.resolvers = {
  Query: {
    ...consoleResolvers,
    ...storyResolvers,
  },
};
