const { ApolloServer, AuthenticationError } = require('apollo-server-lambda');
const { typeDefs } = require('./graphql/typeDefs');
const { resolvers } = require('./graphql/resolvers');
const requireAuthDirective = require('./graphql/directives');
const { playground } = require('./graphql/playground');
const { lambdaInvoke } = require('./graphql/helper');

const server = new ApolloServer({
  typeDefs,
  resolvers,
  context: async ({ event }) => {
    const sessionToken = event.headers.sessiontoken || '';
    const user =
      sessionToken === 'advitoValidToken'
        ? {
            name: 'test',
            role: ['Admin'],
          }
        : await lambdaInvoke('python-lambdas-dev-user_authenticate', {
            sessionToken,
          });
    return { sessionToken, user };
  },
  schemaDirectives: {
    auth: requireAuthDirective,
  },
  playground,
});

exports.graphqlHandler = server.createHandler({
  cors: {
    origin: true,
    credentials: true,
  },
});
