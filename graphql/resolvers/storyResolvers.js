const {
  airSummary,
  trafficLaneOverview,
  topAirlines,
  cabinUse,
  routes,
} = require('../../data/airData');

const {
  hotelSummary,
  hotelSpend,
  topHotelChains,
  topHotelTiers,
  roomNights,
} = require('../../data/hotelData');

const { generateResponse } = require('../helper');

exports.storyResolvers = {
  airMap: (parent, { title }) => {
    switch (title) {
      case 'airSummary':
        return generateResponse(airSummary);
      case 'trafficLaneOverview':
      default:
        return generateResponse(trafficLaneOverview);
    }
  },
  hotelMap: (parent, { title }) => {
    switch (title) {
      case 'hotelSummary':
        return generateResponse(hotelSummary);
      case 'hotelSpend':
      default:
        return generateResponse(hotelSpend);
    }
  },
  visual: (parent, { title }) => {
    switch (title) {
      case 'topAirlines':
        return generateResponse(topAirlines);
      case 'cabinUse':
        return generateResponse(cabinUse);
      case 'topHotelChains':
        return generateResponse(topHotelChains);
      case 'topHotelTiers':
        return generateResponse(topHotelTiers);
      default:
        return null;
    }
  },
  donut: (parent, { title }) => {
    switch (title) {
      case 'airRoot':
        return generateResponse(routes.airRoot);
      case 'transatlantic':
        return generateResponse(routes.transatlantic);
      case 'unitedStates':
        return generateResponse(routes.unitedStates);
      case 'jfk':
        return generateResponse(routes.jfk);
      case 'hotelRoot':
        return generateResponse(roomNights.hotelRoot);
      case 'europe':
        return generateResponse(roomNights.europe);
      case 'unitedKingdom':
        return generateResponse(roomNights.unitedKingdom);
      default:
        return generateResponse(routes.airRoot);
    }
  },
};
