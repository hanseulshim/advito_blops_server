const { gql } = require('apollo-server-hapi');

module.exports = gql`
type Hotel {
  hotelId: Int,
  hotelName: String,
  address: String,
  city: String,
  state: String,
  latitude: String,
  longitude: String
}
type Query {
  hotels: [Hotel]
  hotel(hotelId: Int): Hotel
}
`;