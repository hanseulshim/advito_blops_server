const Hotel = require('../models/Hotel');

module.exports = {
  Query: {
    hotels: () => Hotel.find(),
    hotel: (obj, args) => Hotel.findOne({ hotelId: args.hotelId }),
  },
  Mutation: {
    addHotel: (obj, args) => new Hotel({
      hotelId: args.hotelId,
      hotelName: args.hotelName,
      address: args.address,
      city: args.city,
      state: args.state,
      latitude: args.latitude,
      longitude: args.longitude
    }).save()
  }
};