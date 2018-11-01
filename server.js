const hapi = require('hapi');
const mongoose = require('mongoose');
const Hotel = require('./models/Hotel');

mongoose.connect('mongodb://hshim:B00stlabs!@ds249233.mlab.com:49233/advito_blops_server');
mongoose.connection.once('open', () => console.log('connected to database'));

const server = hapi.server({
  host:'localhost',
  port:8000
});

server.route([
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

const start = async () => {
  try {
      await server.start();
  }
  catch (err) {
      console.log(err);
      process.exit(1);
  }
  console.log('Server running at:', server.info.uri);
};

start();