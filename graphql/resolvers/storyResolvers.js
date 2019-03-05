const { lambdaInvoke } = require('../helper');
// TODO: DELETE HARD-CODED CLIENTID
// Either the call doesn't need it or the user verify call needs to return one
exports.storyResolvers = {
  airMap: (_, { title, ...payload }, { sessionToken, user }) => {
    switch (title) {
      case 'airSummary':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_air',
          {
            ...payload,
            sessionToken,
          },
          'udf_story_air',
        );
      case 'trafficLaneOverview':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_air_traffic',
          {
            ...payload,
            sessionToken,
          },
          'udf_story_air_traffic',
        );
      default:
        return null;
    }
  },
  hotelMap: (_, { title, ...payload }, { sessionToken, user }) => {
    switch (title) {
      case 'hotelSummary':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_hotel',
          {
            ...payload,
            sessionToken,
          },
          'udf_story_hotel',
        );
      case 'hotelSpend':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_hotel_1',
          {
            ...payload,
            sessionToken,
          },
          'udf_story_hotel_1',
        );
      default:
        return null;
    }
  },
  visual: (_, { title, ...payload }, { sessionToken, user }) => {
    switch (title) {
      case 'topAirlines':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_air_airlines',
          {
            ...payload,
            sessionToken,
          },
          'udf_story_air_airlines',
        );
      case 'cabinUse':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_air_cabins',
          {
            ...payload,
            sessionToken,
          },
          'udf_story_air_cabins',
        );
      case 'topHotelChains':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_hotel_2',
          {
            ...payload,
            sessionToken,
          },
          'udf_story_hotel_2',
        );
      case 'topHotelTiers':
        return lambdaInvoke(
          'python-lambdas-dev-udf_story_hotel_3',
          {
            ...payload,
            sessionToken,
          },
          'udf_story_hotel_3',
        );
      default:
        return null;
    }
  },
  donut: async (_, { title, ...payload }, { sessionToken, user }) => {
    switch (title) {
      case 'airRoot':
      case 'transatlantic':
      case 'unitedStates':
        return await lambdaInvoke(
          'python-lambdas-dev-udf_story_air_routes',
          {
            ...payload,
            sessionToken,
          },
          'udf_story_air_routes',
          title,
        );
      case 'jfk':
        const airResponse = await lambdaInvoke(
          'python-lambdas-dev-udf_story_air_routes',
          {
            ...payload,
            sessionToken,
          },
          'udf_story_air_routes',
          title,
        );
        airResponse.last = true;
        airResponse.donutData = airResponse.donutData.map(v => ({
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
            sessionToken,
          },
          'udf_story_hotel_4',
          title,
        );
      default:
        null;
    }
  },
};
