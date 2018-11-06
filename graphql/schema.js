const graphql = require('graphql');
const HotelType = require('./HotelType');
const {
  GraphQLObjectType,
  GraphQLInt,
  GraphQLSchema
} = graphql;

const RootQuery = new GraphQLObjectType({
  name: 'RootQueryType',
  fields: {
    hotel: {
      type: HotelType,
      args: { hotelId: { type: GraphQLInt } },
      resolve(parent, args) {

      }
    }
  }
});

module.exports = new GraphQLSchema({
  query: RootQuery
});
