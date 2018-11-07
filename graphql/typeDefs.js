const { gql } = require('apollo-server-hapi');

module.exports = gql `
type Hotel {
  hotelId: Int,
  hotelName: String,
  address: String,
  city: String,
  state: String,
  latitude: Float,
  longitude: Float
}
type Query {
  hotels: [Hotel],
  hotel(hotelId: Int): Hotel
}
type Mutation {
  addHotel(hotelId: Int,
    hotelName: String,
    address: String,
    city: String,
    state: String,
    latitude: Float,
    longitude: Float): Hotel
}
`;