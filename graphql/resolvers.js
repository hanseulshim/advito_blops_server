const Hotel = require('../models/Hotel');

module.exports = {
  Query: {
    hotels: () => Hotel.find(),
    hotel: (obj, args) => Hotel.findOne({ hotelId: args.hotelId }),
  },
};