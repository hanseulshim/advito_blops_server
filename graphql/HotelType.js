const graphql = require('graphql');

const { GraphQLObjectType, GraphQLString, GraphQLFloat, GraphQLInt } = graphql;

const HotelType = new GraphQLObjectType({
  name: 'Hotel',
  fields: () => ({
    hotelId: { type: GraphQLInt },
    hotelName: { type: GraphQLString },
    address: { type: GraphQLString },
    city: { type: GraphQLString },
    state: { type: GraphQLString },
    latitude: { type: GraphQLFloat },
    longitude: { type: GraphQLFloat }
  })
});

module.exports = HotelType;
