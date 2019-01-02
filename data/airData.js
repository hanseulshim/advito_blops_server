exports.airSummary = {
  title: 'Air Summary',
  summary:
    '2017 was a busy year. Your company flew 3.18M miles, or 6.1M km between 12 countries. Deal makers comprised of the most spend and miles traveled, while Executives saved the most.',
  kpis: [
    {
      title: 'Spend',
      value: 2400000,
      delta: 190500,
      change: '-',
      type: 'money',
      icon: 'spend_icon.png',
    },
    {
      title: 'Tickets',
      value: 2690,
      delta: 341,
      change: '+',
      type: '',
      icon: 'tickets_icon.png',
    },
    {
      title: 'Savings',
      value: 144000,
      delta: 12200,
      change: '+',
      type: 'money',
      icon: 'savings_icon.png',
    },
    {
      title: 'Miles Traveled',
      value: 3180000,
      delta: 541000,
      change: '+',
      type: '',
      icon: 'miles_icon.png',
    },
    {
      title: 'Countries Visited',
      value: 12,
      delta: 1,
      change: '+',
      type: '',
      icon: 'countries_icon.png',
    },
    {
      title: 'Emissions',
      value: 159,
      delta: 2.2,
      change: '+',
      type: 'emissions',
      icon: 'emissions_icon.png',
    },
  ],
  barchart: [
    {
      title: 'Spend',
      type: 'money',
      data: [
        {
          category: 'Deal Maker',
          value: 25000,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 12000,
          change: '+',
        },
        {
          category: 'Executive',
          value: 10000,
          change: '+',
        },
        {
          category: 'On Demand',
          value: 9200,
          change: '+',
        },
      ],
    },
    {
      title: 'Tickets',
      type: '',
      data: [
        {
          category: 'Deal Maker',
          value: 204,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 56,
          change: '+',
        },
        {
          category: 'Executive',
          value: 100,
          change: '-',
        },
        {
          category: 'On Demand',
          value: 37,
          change: '+',
        },
      ],
    },
    {
      title: 'Savings',
      type: 'money',
      data: [
        {
          category: 'Deal Maker',
          value: 3500,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 3700,
          change: '+',
        },
        {
          category: 'Executive',
          value: 2100,
          change: '-',
        },
        {
          category: 'On Demand',
          value: 1300,
          change: '+',
        },
      ],
    },
    {
      title: 'Miles Traveled',
      type: '',
      data: [
        {
          category: 'Deal Maker',
          value: 35000,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 56200,
          change: '+',
        },
        {
          category: 'Executive',
          value: 10000,
          change: '-',
        },
        {
          category: 'On Demand',
          value: 13200,
          change: '-',
        },
      ],
    },
    {
      title: 'Countries Visited',
      type: '',
      data: [
        {
          category: 'Deal Maker',
          value: 6,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 2,
          change: '+',
        },
        {
          category: 'Executive',
          value: 2,
          change: '-',
        },
        {
          category: 'On Demand',
          value: 4,
          change: '-',
        },
      ],
    },
    {
      title: 'Emissions',
      type: '',
      data: [
        {
          category: 'Deal Maker',
          value: 5.5,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 2.5,
          change: '+',
        },
        {
          category: 'Executive',
          value: 1.4,
          change: '-',
        },
        {
          category: 'On Demand',
          value: 2.7,
          change: '+',
        },
      ],
    },
  ],
  locations: [
    {
      thickness: 50,
      height: 0.4,
      opacity: 0.7,
      coords: [
        {
          latitude: 19.42847,
          longitude: -99.12766,
        },
        {
          latitude: 48.85341,
          longitude: 2.3488,
        },
      ],
      from: 'MEX',
      to: 'CDG',
    },
    {
      thickness: 10,
      height: 0.5,
      opacity: 1,
      coords: [
        {
          latitude: 19.42847,
          longitude: -99.12766,
        },
        {
          latitude: 25.0657,
          longitude: 55.17128,
        },
      ],
      from: 'MEX',
      to: 'DWC',
    },
    {
      thickness: 5,
      height: 0.45,
      opacity: 0.3,
      coords: [
        {
          latitude: 19.42847,
          longitude: -99.12766,
        },
        { latitude: 37.566, longitude: 126.9784 },
      ],
      from: 'MEX',
      to: 'GMP',
    },
    {
      thickness: 5,
      height: 0.7,
      opacity: 1,
      coords: [
        { latitude: 34.05223, longitude: -118.24368 },
        { latitude: 40.71427, longitude: -74.00597 },
      ],
      from: 'LAX',
      to: 'JFK',
    },
    {
      thickness: 75,
      height: 0.5,
      opacity: 0.4,
      coords: [
        { latitude: 34.05223, longitude: -118.24368 },
        { latitude: 40.416500000000006, longitude: -3.70256 },
      ],
      from: 'LAX',
      to: 'MAD',
    },
    {
      thickness: 30,
      height: 0.6,
      opacity: 0.8,
      coords: [
        { latitude: -15.779720000000001, longitude: -47.92972 },
        { latitude: 39.9075, longitude: 116.39723 },
      ],
      from: 'BSB',
      to: 'PEK',
    },
  ],
};

exports.trafficLaneOverview = {
  title: 'Traffic Lane Overview',
  summary:
    'The traffic lane with the most tickets was US Domestic.It was also the cheapest per mile and saved the most. The least efficient traffic lane was US MEA.',
  kpis: [
    {
      title: 'US Domestic',
      value: 126000,
      delta: 1500,
      change: '-',
      type: 'money',
      icon: 'spend_icon.png',
    },
    {
      title: 'Intra Europe',
      value: 101000,
      delta: 8200,
      change: '+',
      type: 'money',
      icon: 'spend_icon.png',
    },
    {
      title: 'Intra Asia',
      value: 98400,
      delta: 12200,
      change: '+',
      type: 'money',
      icon: 'spend_icon.png',
    },
    {
      title: 'Transatlantic',
      value: 92600,
      delta: 1900,
      change: '+',
      type: 'money',
      icon: 'spend_icon.png',
    },
    {
      title: 'Transpacific',
      value: 60900,
      delta: 4100,
      change: '+',
      type: 'money',
      icon: 'spend_icon.png',
    },
    {
      title: 'US MEA',
      value: 44000,
      delta: 2200,
      change: '+',
      type: 'money',
      icon: 'spend_icon.png',
    },
  ],
  barchart: [
    {
      title: 'Spend',
      type: 'money',
      data: [
        {
          category: 'US Domestic',
          value: 25000,
          change: '+',
        },
        {
          category: 'Intra Europe',
          value: 12000,
          change: '+',
        },
        {
          category: 'Intra Asia',
          value: 10000,
          change: '+',
        },
        {
          category: 'Transatlantic',
          value: 9200,
          change: '+',
        },
        {
          category: 'Transpacific',
          value: 6100,
          change: '+',
        },
        {
          category: 'US MEA',
          value: 4000,
          change: '+',
        },
      ],
    },
    {
      title: 'Tickets',
      type: '',
      data: [
        {
          category: 'US Domestic',
          value: 402,
          change: '+',
        },
        {
          category: 'Intra Europe',
          value: 54,
          change: '-',
        },
        {
          category: 'Intra Asia',
          value: 89,
          change: '+',
        },
        {
          category: 'Transatlantic',
          value: 46,
          change: '-',
        },
        {
          category: 'Transpacific',
          value: 43,
          change: '+',
        },
        {
          category: 'US MEA',
          value: 28,
          change: '+',
        },
      ],
    },
    {
      title: 'Savings',
      type: 'money',
      data: [
        {
          category: 'US Domestic',
          value: 4400,
          change: '+',
        },
        {
          category: 'Intra Europe',
          value: 1500,
          change: '+',
        },
        {
          category: 'Intra Asia',
          value: 1100,
          change: '+',
        },
        {
          category: 'Transatlantic',
          value: 900,
          change: '-',
        },
        {
          category: 'Transpacific',
          value: 650,
          change: '+',
        },
        {
          category: 'US MEA',
          value: 450,
          change: '+',
        },
      ],
    },
    {
      title: 'Cost Per Mile',
      type: 'money',
      data: [
        {
          category: 'US Domestic',
          value: 18.5,
          change: '+',
        },
        {
          category: 'Intra Europe',
          value: 12.2,
          change: '+',
        },
        {
          category: 'Intra Asia',
          value: 10.1,
          change: '+',
        },
        {
          category: 'Transatlantic',
          value: 5.96,
          change: '-',
        },
        {
          category: 'Transpacific',
          value: 1.25,
          change: '+',
        },
        {
          category: 'US MEA',
          value: 0.59,
          change: '+',
        },
      ],
    },
  ],
  locations: [
    {
      thickness: 50,
      height: 0.4,
      opacity: 0.7,
      coords: [
        {
          latitude: 19.42847,
          longitude: -99.12766,
        },
        {
          latitude: 48.85341,
          longitude: 2.3488,
        },
      ],
      from: 'MEX',
      to: 'CDG',
    },
    {
      thickness: 10,
      height: 0.5,
      opacity: 1,
      coords: [
        {
          latitude: 19.42847,
          longitude: -99.12766,
        },
        {
          latitude: 25.0657,
          longitude: 55.17128,
        },
      ],
      from: 'MEX',
      to: 'DWC',
    },
    {
      thickness: 5,
      height: 0.45,
      opacity: 0.3,
      coords: [
        {
          latitude: 19.42847,
          longitude: -99.12766,
        },
        { latitude: 37.566, longitude: 126.9784 },
      ],
      from: 'MEX',
      to: 'GMP',
    },
    {
      thickness: 5,
      height: 0.7,
      opacity: 1,
      coords: [
        { latitude: 34.05223, longitude: -118.24368 },
        { latitude: 40.71427, longitude: -74.00597 },
      ],
      from: 'LAX',
      to: 'JFK',
    },
    {
      thickness: 75,
      height: 0.5,
      opacity: 0.4,
      coords: [
        { latitude: 34.05223, longitude: -118.24368 },
        { latitude: 40.416500000000006, longitude: -3.70256 },
      ],
      from: 'LAX',
      to: 'MAD',
    },
    {
      thickness: 30,
      height: 0.6,
      opacity: 0.8,
      coords: [
        { latitude: -15.779720000000001, longitude: -47.92972 },
        { latitude: 39.9075, longitude: 116.39723 },
      ],
      from: 'BSB',
      to: 'PEK',
    },
  ],
};

exports.topAirlines = {
  title: 'Top Airlines',
  summary:
    'The top airline by net effective savings ratio was Lufthansa at 16.2%. The airline that saw the largest increase in net effective savings ratio was Lufthansa while the airline that saw the largest decrease was Southwest.',
  barchart: [],
  categories: [
    {
      title: 'Spend',
      icon: 'spend_icon.png',
      total: 1325877,
      subCategories: [
        {
          name: 'British Airways',
          value: 185601,
          delta: 0,
          color: '#032F56',
        },
        {
          name: 'Finnair',
          value: 360960,
          delta: 0,
          color: '#085887',
        },
        {
          name: 'Lufthansa',
          value: 185601,
          delta: 0,
          color: '#226F9D',
        },
        {
          name: 'Singapore Airlines',
          value: 176690,
          delta: 0,
          color: '#468Ab2',
        },
        {
          name: 'Air France',
          value: 290560,
          delta: 0,
          color: '#63a0c4',
        },
        {
          name: 'Other',
          value: 126465,
          delta: 0,
          color: '#8dc6e7',
        },
      ],
    },
    {
      title: 'Tickets',
      icon: 'tickets_icon.png',
      total: 2508,
      subCategories: [
        {
          name: 'British Airways',
          value: 290,
          delta: 0,
          color: '#032F56',
        },
        {
          name: 'Finnair',
          value: 564,
          delta: 0,
          color: '#085887',
        },
        {
          name: 'Lufthansa',
          value: 670,
          delta: 0,
          color: '#226F9D',
        },
        {
          name: 'Singapore Airlines',
          value: 207,
          delta: 0,
          color: '#468Ab2',
        },
        {
          name: 'Air France',
          value: 579,
          delta: 0,
          color: '#63a0c4',
        },
        {
          name: 'Other',
          value: 198,
          delta: 0,
          color: '#8dc6e7',
        },
      ],
    },
    {
      title: 'Savings',
      icon: 'savings_icon.png',
      total: 117211,
      subCategories: [
        {
          name: 'British Airways',
          value: 25601,
          delta: 5300,
          color: '#032F56',
        },
        {
          name: 'Finnair',
          value: 20960,
          delta: 2000,
          color: '#085887',
        },
        {
          name: 'Lufthansa',
          value: 20960,
          delta: 1200,
          color: '#226F9D',
        },
        {
          name: 'Singapore Airlines',
          value: 15480,
          delta: 400,
          color: '#468Ab2',
        },
        {
          name: 'Air France',
          value: 19560,
          delta: 2200,
          color: '#63a0c4',
        },
        {
          name: 'Other',
          value: 14650,
          delta: 300,
          color: '#8dc6e7',
        },
      ],
    },
  ],
};

exports.cabinUse = {
  title: 'Cabin Use',
  summary:
    'The top cabin, across all personas in 2018, was Premium Economy at $428,800 (670 tickets) and $48,800 in savings. This was the largest increase from last year at 13%.',
  barchart: [
    {
      title: 'First Class',
      type: 'money',
      data: [
        {
          category: 'Deal Maker',
          change: '+',
          value: 25000,
        },
        {
          category: 'Road Warrior',
          change: '+',
          value: 12000,
        },
        {
          category: 'Executive',
          change: '+',
          value: 10000,
        },
        {
          category: 'On Demand',
          change: '+',
          value: 9200,
        },
      ],
    },
    {
      title: 'Business',
      type: 'money',
      data: [
        {
          category: 'Deal Maker',
          change: '+',
          value: 4400,
        },
        {
          category: 'Road Warrior',
          change: '+',
          value: 1500,
        },
        {
          category: 'Executive',
          change: '+',
          value: 1100,
        },
        {
          category: 'On Demand',
          change: '-',
          value: 900,
        },
      ],
    },
    {
      title: 'Premium Economy',
      type: 'money',
      data: [
        {
          category: 'Deal Maker',
          change: '+',
          value: 2300,
        },
        {
          category: 'Road Warrior',
          change: '+',
          value: 1200,
        },
        {
          category: 'Executive',
          change: '+',
          value: 2400,
        },
        {
          category: 'On Demand',
          change: '-',
          value: 1300,
        },
      ],
    },
    {
      title: 'Economy',
      type: 'money',
      data: [
        {
          category: 'Deal Maker',
          change: '+',
          value: 2500,
        },
        {
          category: 'Road Warrior',
          change: '+',
          value: 1500,
        },
        {
          category: 'Executive',
          change: '+',
          value: 1100,
        },
        {
          category: 'On Demand',
          change: '-',
          value: 690,
        },
      ],
    },
  ],
  categories: [
    {
      title: 'Spend',
      icon: 'spend_icon.png',
      total: 908852,
      subCategories: [
        {
          name: 'First Class',
          value: 176690,
          delta: 0,
          color: '#8DC6e7',
        },
        {
          name: 'Business',
          value: 360960,
          delta: 0,
          color: '#468ab2',
        },
        {
          name: 'Premium Economy',
          value: 185601,
          delta: 0,
          color: '#085887',
        },
        {
          name: 'Economy',
          value: 185601,
          delta: 0,
          color: '#032f56',
        },
      ],
    },
    {
      title: 'Tickets',
      icon: 'tickets_icon.png',
      total: 2616,
      subCategories: [
        {
          name: 'First Class',
          value: 403,
          delta: 0,
          color: '#8DC6e7',
        },
        {
          name: 'Business',
          value: 400,
          delta: 0,
          color: '#468ab2',
        },
        {
          name: 'Premium Economy',
          value: 843,
          delta: 0,
          color: '#085887',
        },
        {
          name: 'Economy',
          value: 970,
          delta: 0,
          color: '#032f56',
        },
      ],
    },
    {
      title: 'Savings',
      icon: 'savings_icon.png',
      total: 108160,
      subCategories: [
        {
          name: 'First Class',
          value: 19560,
          delta: 500,
          color: '#8DC6e7',
        },
        {
          name: 'Business',
          value: 48000,
          delta: 3200,
          color: '#468ab2',
        },
        {
          name: 'Premium Economy',
          value: 15480,
          delta: 1200,
          color: '#085887',
        },
        {
          name: 'Economy',
          value: 25120,
          delta: 1400,
          color: '#032f56',
        },
      ],
    },
  ],
};

exports.routeTypes = {
  title: 'Airline Tickets by Route Types',
  summary:
    'Us Domestic was the most frequently flown route type, accounting for 27% of the total tickets purchased in 2018. This was a 2% increase over 2017',
  level: 'All Routes',
  data: [
    {
      category: 'US Domestic',
      value: 18,
      prop: 'routes',
    },
    {
      category: 'Transpacific',
      value: 27,
      prop: 'routes',
      nextProp: 'countries',
    },
    {
      category: 'Intra Europe',
      value: 11,
      prop: 'routes',
    },
    {
      category: 'US MEA',
      value: 20,
      prop: 'routes',
    },
    {
      category: 'Intra Asia',
      value: 8,
      prop: 'routes',
    },
    {
      category: 'Transatlantic',
      value: 5,
      prop: 'routes',
    },
  ],
  countries: [
    {
      category: 'United Kingdom',
      value: 21,
      prop: 'countries',
    },
    {
      category: 'Norway',
      value: 18,
      prop: 'countries',
    },
    {
      category: 'Germany',
      value: 10,
      prop: 'countries',
    },
    {
      category: 'France',
      value: 11,
      prop: 'countries',
    },
    {
      category: 'Spain',
      value: 5,
      prop: 'countries',
    },
    {
      category: 'United States',
      value: 3,
      prop: 'countries',
      nextProp: 'airports',
    },
    {
      category: 'United Arab Emirates',
      value: 32,
      prop: 'countries',
    },
  ],
  airports: [
    {
      category: 'ATL',
      value: 22,
      prop: 'airports',
    },
    {
      category: 'ORD',
      value: 18,
      prop: 'airports',
    },
    {
      category: 'JFK',
      value: 11,
      prop: 'airports',
    },
    {
      category: 'LGA',
      value: 11,
      prop: 'airports',
    },
    {
      category: 'DFW',
      value: 7,
      prop: 'airports',
    },
    {
      category: 'DIA',
      value: 4,
      prop: 'airports',
    },
    {
      category: 'LAX',
      value: 27,
      prop: 'airports',
    },
  ],
};
