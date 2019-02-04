const { consoleResolvers } = require('./consoleResolvers');
const { storyResolvers } = require('./storyResolvers');
const { generateResponse } = require('../helper');

exports.resolvers = {
  Query: {
    ...consoleResolvers,
    ...storyResolvers,
    login: () =>
      generateResponse({
        displayName: 'Jonathan Smith',
        clientId: 125,
        profilePicturePath: 'test',
        sessionToken: 'dfobiajdfobi',
      }),
  },
};
