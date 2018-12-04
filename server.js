const { ApolloServer, gql } = require('apollo-server');
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
});

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});
