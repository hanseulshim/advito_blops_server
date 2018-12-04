const { ApolloServer } = require('apollo-server-lambda');
const { typeDefs } = require('./graphql/typeDefs');
const { resolvers } = require('./graphql/resolvers');

const resolvers = {
  Query: {
    scott: () => 'boss',
    john: () => 'lil johnny!',
    shayan: () => 'call linda asap!',
    hanseul: () => 'han solo!',
    activeAlerts: () => activeAlerts,
    upcomingActions: () => upcomingActions,
  },
};

const server = new ApolloServer({
  typeDefs,
  resolvers,
  introspection: true,
  playground: {
    settings: {
      'editor.cursorShape': 'line',
    },
  },
});

exports.graphqlHandler = server.createHandler({
  cors: {
    origin: true,
    credentials: true,
  },
});
