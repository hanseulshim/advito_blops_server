const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const HotelSchema = new Schema({
  hotelId: Number,
  hotelName: String,
  address: String,
  city: String,
  state: String,
  latitude: Number,
  longitude: Number
});

module.exports = mongoose.model('Hotel', HotelSchema);