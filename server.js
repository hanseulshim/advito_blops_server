const Hapi = require('hapi');
const { ApolloServer, gql } = require('apollo-server-hapi');
const mongoose = require('mongoose');

const resolvers = require('./graphql/resolvers');
const typeDefs = require('./graphql/typeDefs');

mongoose.connect('mongodb://hshim:B00stlabs!@ds249233.mlab.com:49233/advito_blops_server', { useNewUrlParser: true });
mongoose.connection.once('open', () => console.log('connected to database'));

const startServer = async () => {
  const server = new ApolloServer({ typeDefs, resolvers });
  const app = new Hapi.server({ port: 4000 });

  await server.applyMiddleware({ app });
  await server.installSubscriptionHandlers(app.listener);

  try {
    await app.start();
  }
  catch (err) {
      console.log(err);
      process.exit(1);
  }
  console.log('Server running at:', app.info.uri);
};

startServer();