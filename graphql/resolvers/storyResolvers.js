const {
  airSummary,
  trafficLaneOverview,
  topAirlines,
  cabinUse,
} = require('../../data/airData');

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
  airPlane: (parent, { title }) => {
    switch (title) {
      case 'topAirlines':
        return topAirlines;
      case 'cabinUse':
      default:
        return cabinUse;
    }
  },
};
