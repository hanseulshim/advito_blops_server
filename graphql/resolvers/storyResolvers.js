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

exports.storyResolvers = {
  airMap: (parent, { title }) => {
    switch (title) {
      case 'airSummary':
        return airSummary;
      case 'trafficLaneOverview':
      default:
        return trafficLaneOverview;
    }
  },
  hotelMap: (parent, { title }) => {
    switch (title) {
      case 'hotelSummary':
        return hotelSummary;
      case 'hotelSpend':
      default:
        return hotelSpend;
    }
  },
  visual: (parent, { title }) => {
    switch (title) {
      case 'topAirlines':
        return topAirlines;
      case 'cabinUse':
        return cabinUse;
      case 'topHotelChains':
        return topHotelChains;
      case 'topHotelTiers':
        return topHotelTiers;
      default:
        return null;
    }
  },
  donut: (parent, { title }) => {
    switch (title) {
      case 'airRoot':
        return routes.airRoot;
      case 'transatlantic':
        return routes.transatlantic;
      case 'unitedStates':
        return routes.unitedStates;
      case 'jfk':
        return routes.jfk;
      case 'hotelRoot':
        return roomNights.hotelRoot;
      case 'europe':
        return roomNights.europe;
      case 'unitedKingdom':
        return roomNights.unitedKingdom;
      default:
        return routes.airRoot;
    }
  },
};
