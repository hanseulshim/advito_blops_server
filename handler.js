const { ApolloServer, gql } = require('apollo-server-lambda');

const typeDefs = gql`
  type Query {
    scott: String
    john: String
    shayan: String
    hanseul: String
  }
`;

const resolvers = {
  Query: {
    scott: () => 'Boss man!',
    john: () => 'lil johnny!',
    shayan: () => 'call linda asap!',
    hanseul: () => 'han solo!',
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

exports.graphqlHandler = server.createHandler();
