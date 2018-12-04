const { ApolloServer, gql } = require('apollo-server-lambda');
const { activeAlerts, upcomingActions } = require('./data/sidebarData');

const typeDefs = gql`
  type Action {
    header: String
    secondaryHeader: String
    icon: String
    alert: Boolean
  }

  type Query {
    scott: String
    john: String
    shayan: String
    hanseul: String
    activeAlerts: [Action]
    upcomingActions: [Action]
  }
`;

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
