const Hapi = require('hapi');
const { ApolloServer, gql } = require('apollo-server-hapi');
const mongoose = require('mongoose');

const schema = require ('./graphql/schema');
const Hotel = require('./models/Hotel');

mongoose.connect('mongodb://hshim:B00stlabs!@ds249233.mlab.com:49233/advito_blops_server', { useNewUrlParser: true });
mongoose.connection.once('open', () => console.log('connected to database'));

const typeDefs = gql`
  # Comments in GraphQL are defined with the hash (#) symbol.

  # This "Book" type can be used in other type declarations.
  type Hotel {
    hotelId: Int,
    hotelName: String,
    address: String,
    city: String,
    state: String,
    latitude: String,
    longitude: String
  }

  # The "Query" type is the root of all GraphQL queries.
  # (A "Mutation" type will be covered later on.)
  type Query {
    hotels: [Hotel]
  }
`;

const resolvers = {
  Query: {
    hotels: () => Hotel.find(),
  },
};

const startServer = async () => {
  const server = new ApolloServer({ typeDefs, resolvers });

  const app = new Hapi.server({
    port: 4000
  });

  await server.applyMiddleware({
    app,
  });

  await server.installSubscriptionHandlers(app.listener);

  try {
      await app.start();
      app.route([
        {
          method: 'GET',
          path: '/',
          handler: (req, h) => {
            return '<h1>This is my server</h1>';
          }
        },
        {
          method: 'GET',
          path: '/api/v1/hotels',
          handler: (req, h) => {
            return Hotel.find();
          }
        },
        {
          method: 'POST',
          path: '/api/v1/hotels',
          handler: (req, h) => {
            const { hotelId, hotelName, address, city, state, latitude, longitude } = req.payload;
            const hotel = new Hotel({
              hotelId,
              hotelName,
              address,
              city,
              state,
              latitude,
              longitude
            });
            return hotel.save();
          }
        },
      ]);
  }
  catch (err) {
      console.log(err);
      process.exit(1);
  }
  console.log('Server running at:', app.info.uri);
};

startServer();