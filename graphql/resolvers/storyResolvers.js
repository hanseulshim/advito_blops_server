// TODO: delete these eventually
// const {
//   airSummary,
//   trafficLaneOverview,
//   topAirlines,
//   cabinUse,
//   routes,
// } = require('../../data/airData');

// const {
//   hotelSummary,
//   hotelSpend,
//   topHotelChains,
//   topHotelTiers,
//   roomNights,
// } = require('../../data/hotelData');

const { lambdaInvoke } = require('../helper');

exports.storyResolvers = {
  airMap: (_, { title, ...payload }) => {
    switch (title) {
      case 'airSummary':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_air',
          {
            ...payload,
          },
          'udf_story_air'
        );
      case 'trafficLaneOverview':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_air_traffic',
          {
            ...payload,
          },
          'udf_story_air_traffic'
        );
      default:
        return null;
    }
  },
  hotelMap: (_, { title, ...payload }) => {
    switch (title) {
      case 'hotelSummary':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_hotel',
          {
            ...payload,
          },
          'udf_story_hotel'
        );
      case 'hotelSpend':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_hotel_1',
          {
            ...payload,
          },
          'udf_story_hotel_1'
        );
      default:
        return null;
    }
  },
  visual: (_, { title, ...payload }) => {
    switch (title) {
      case 'topAirlines':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_air_airlines',
          {
            ...payload,
          },
          'udf_story_air_airlines'
        );
      case 'cabinUse':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_air_cabins',
          {
            ...payload,
          },
          'udf_story_air_cabins'
        );
      case 'topHotelChains':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_hotel_2',
          {
            ...payload,
          },
          'udf_story_hotel_2'
        );
      case 'topHotelTiers':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_hotel_3',
          {
            ...payload,
          },
          'udf_story_hotel_3'
        );
      default:
        return null;
    }
  },
  donut: async (_, { title, ...payload }) => {
    switch (title) {
      case 'airRoot':
      case 'transatlantic':
      case 'unitedStates':
        return await lambdaInvoke(
          'python-lambdas-dev-udf_story_air_routes',
          {
            ...payload,
          },
          'udf_story_air_routes',
          title
        );
      case 'jfk':
        const airResponse = await lambdaInvoke(
          'python-lambdas-dev-udf_story_air_routes',
          {
            ...payload,
          },
          'udf_story_air_routes',
          title
        );
        const dataset = airResponse.body.apidataset;
        dataset.last = true;
        dataset.donutData = dataset.donutData.map(v => ({
          ...v,
          tooltip: {
            title: 'TOP AIRLINES',
            tooltipData: [
              {
                name: 'British Airways',
                value: Math.floor(Math.random() * 100) / 100,
              },
              {
                name: 'Lufthansa',
                value: Math.floor(Math.random() * 100) / 100,
              },
              {
                name: 'KLM',
                value: Math.floor(Math.random() * 100) / 100,
              },
              {
                name: 'Singapore Airlines',
                value: Math.floor(Math.random() * 100) / 100,
              },
              {
                name: 'Other',
                value: Math.floor(Math.random() * 100) / 100,
              },
            ],
          },
        }));
        return airResponse;
      case 'hotelRoot':
      case 'europe':
      case 'unitedKingdom':
        return await lambdaInvoke(
          'python-lambdas-dev-udf_story_hotel_4',
          {
            ...payload,
          },
          'udf_story_hotel_4',
          title
        );
      default:
        null;
    }
  },
};
