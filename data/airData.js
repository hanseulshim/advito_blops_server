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
          value: 500000,
          delta: 25000,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 300000,
          delta: 12000,
          change: '+',
        },
        {
          category: 'Executive',
          value: 400000,
          delta: 10000,
          change: '+',
        },
        {
          category: 'On Demand',
          value: 200000,
          delta: 9200,
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
          value: 300,
          delta: 204,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 250,
          delta: 56,
          change: '+',
        },
        {
          category: 'Executive',
          value: 200,
          delta: 100,
          change: '-',
        },
        {
          category: 'On Demand',
          value: 250,
          delta: 37,
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
          value: 30000,
          delta: 3500,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 31000,
          delta: 3700,
          change: '+',
        },
        {
          category: 'Executive',
          value: 35000,
          delta: 2100,
          change: '-',
        },
        {
          category: 'On Demand',
          value: 31000,
          delta: 1300,
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
          value: 100000,
          delta: 35000,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 80000,
          delta: 56200,
          change: '+',
        },
        {
          category: 'Executive',
          value: 80000,
          delta: 10000,
          change: '-',
        },
        {
          category: 'On Demand',
          value: 90000,
          delta: 13200,
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
          value: 5,
          delta: 6,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 7,
          delta: 2,
          change: '+',
        },
        {
          category: 'Executive',
          value: 6,
          delta: 2,
          change: '-',
        },
        {
          category: 'On Demand',
          value: 4,
          delta: 4,
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
          delta: 5.5,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 7.5,
          delta: 2.5,
          change: '+',
        },
        {
          category: 'Executive',
          value: 6.5,
          delta: 1.4,
          change: '-',
        },
        {
          category: 'On Demand',
          value: 5,
          delta: 2.7,
          change: '+',
        },
      ],
    },
  ],
  locations: [
    {
      thickness: 5,
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
      origin: 'MEX',
      destination: 'CDG',
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
      origin: 'MEX',
      destination: 'DWC',
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
      origin: 'MEX',
      destination: 'GMP',
    },
    {
      thickness: 5,
      height: 0.7,
      opacity: 1,
      coords: [
        { latitude: 34.05223, longitude: -118.24368 },
        { latitude: 40.71427, longitude: -74.00597 },
      ],
      origin: 'LAX',
      destination: 'JFK',
    },
    {
      thickness: 10,
      height: 0.5,
      opacity: 0.4,
      coords: [
        { latitude: 34.05223, longitude: -118.24368 },
        { latitude: 40.416500000000006, longitude: -3.70256 },
      ],
      origin: 'LAX',
      destination: 'MAD',
    },
    {
      thickness: 8,
      height: 0.6,
      opacity: 0.8,
      coords: [
        { latitude: -15.779720000000001, longitude: -47.92972 },
        { latitude: 39.9075, longitude: 116.39723 },
      ],
      origin: 'BSB',
      destination: 'PEK',
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
          value: 50000,
          delta: 25000,
          change: '+',
        },
        {
          category: 'Intra Europe',
          value: 40000,
          delta: 12000,
          change: '+',
        },
        {
          category: 'Intra Asia',
          value: 45000,
          delta: 10000,
          change: '+',
        },
        {
          category: 'Transatlantic',
          value: 30000,
          delta: 9200,
          change: '+',
        },
        {
          category: 'Transpacific',
          value: 35000,
          delta: 6100,
          change: '+',
        },
        {
          category: 'US MEA',
          value: 30000,
          delta: 4000,
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
          value: 100,
          delta: 402,
          change: '+',
        },
        {
          category: 'Intra Europe',
          value: 80,
          delta: 54,
          change: '-',
        },
        {
          category: 'Intra Asia',
          value: 75,
          delta: 89,
          change: '+',
        },
        {
          category: 'Transatlantic',
          value: 85,
          delta: 46,
          change: '-',
        },
        {
          category: 'Transpacific',
          value: 80,
          delta: 43,
          change: '+',
        },
        {
          category: 'US MEA',
          value: 85,
          delta: 28,
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
          value: 5000,
          delta: 4400,
          change: '+',
        },
        {
          category: 'Intra Europe',
          value: 5500,
          delta: 1500,
          change: '+',
        },
        {
          category: 'Intra Asia',
          value: 4500,
          delta: 1100,
          change: '+',
        },
        {
          category: 'Transatlantic',
          value: 4500,
          delta: 900,
          change: '-',
        },
        {
          category: 'Transpacific',
          value: 4000,
          delta: 650,
          change: '+',
        },
        {
          category: 'US MEA',
          value: 5000,
          delta: 450,
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
          delta: 18.5,
          change: '+',
        },
        {
          category: 'Intra Europe',
          value: 16.2,
          delta: 12.2,
          change: '+',
        },
        {
          category: 'Intra Asia',
          value: 17.1,
          delta: 10.1,
          change: '+',
        },
        {
          category: 'Transatlantic',
          value: 15.96,
          delta: 5.96,
          change: '-',
        },
        {
          category: 'Transpacific',
          value: 16.25,
          delta: 1.25,
          change: '+',
        },
        {
          category: 'US MEA',
          value: 14.59,
          delta: 0.59,
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
      origin: 'MEX',
      destination: 'CDG',
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
      origin: 'MEX',
      destination: 'DWC',
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
      origin: 'MEX',
      destination: 'GMP',
    },
    {
      thickness: 5,
      height: 0.7,
      opacity: 1,
      coords: [
        { latitude: 34.05223, longitude: -118.24368 },
        { latitude: 40.71427, longitude: -74.00597 },
      ],
      origin: 'LAX',
      destination: 'JFK',
    },
    {
      thickness: 75,
      height: 0.5,
      opacity: 0.4,
      coords: [
        { latitude: 34.05223, longitude: -118.24368 },
        { latitude: 40.416500000000006, longitude: -3.70256 },
      ],
      origin: 'LAX',
      destination: 'MAD',
    },
    {
      thickness: 30,
      height: 0.6,
      opacity: 0.8,
      coords: [
        { latitude: -15.779720000000001, longitude: -47.92972 },
        { latitude: 39.9075, longitude: 116.39723 },
      ],
      origin: 'BSB',
      destination: 'PEK',
    },
  ],
};

exports.topAirlines = {
  title: 'Top Airlines',
  summary:
    'The top airline by net effective savings ratio was Lufthansa at 16.2%. The airline that saw the largest increase in net effective savings ratio was Lufthansa while the airline that saw the largest decrease was Southwest.',
  categories: [
    {
      title: 'Spend',
      type: 'money',
      icon: 'spend_icon.png',
      total: 1325877,
      subCategories: [
        {
          name: 'British Airways',
          value: 185601,
          color: '#032F56',
        },
        {
          name: 'Finnair',
          value: 360960,
          color: '#085887',
        },
        {
          name: 'Lufthansa',
          value: 185601,
          color: '#226F9D',
        },
        {
          name: 'Singapore Airlines',
          value: 176690,
          color: '#468Ab2',
        },
        {
          name: 'Air France',
          value: 290560,
          color: '#63a0c4',
        },
        {
          name: 'Other',
          value: 126465,
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
          color: '#032F56',
        },
        {
          name: 'Finnair',
          value: 564,
          color: '#085887',
        },
        {
          name: 'Lufthansa',
          value: 670,
          color: '#226F9D',
        },
        {
          name: 'Singapore Airlines',
          value: 207,
          color: '#468Ab2',
        },
        {
          name: 'Air France',
          value: 579,
          color: '#63a0c4',
        },
        {
          name: 'Other',
          value: 198,
          color: '#8dc6e7',
        },
      ],
    },
    {
      title: 'Savings',
      type: 'money',
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
          value: 500000,
          delta: 25000,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 300000,
          delta: 12000,
          change: '+',
        },
        {
          category: 'Executive',
          value: 400000,
          delta: 10000,
          change: '+',
        },
        {
          category: 'On Demand',
          value: 200000,
          delta: 9200,
          change: '+',
        },
      ],
    },
    {
      title: 'Business',
      type: 'money',
      data: [
        {
          category: 'Deal Maker',
          value: 300,
          delta: 204,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 250,
          delta: 56,
          change: '+',
        },
        {
          category: 'Executive',
          value: 200,
          delta: 100,
          change: '-',
        },
        {
          category: 'On Demand',
          value: 250,
          delta: 37,
          change: '+',
        },
      ],
    },
    {
      title: 'Premium Economy',
      type: 'money',
      data: [
        {
          category: 'Deal Maker',
          value: 30000,
          delta: 3500,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 31000,
          delta: 3700,
          change: '+',
        },
        {
          category: 'Executive',
          value: 35000,
          delta: 2100,
          change: '-',
        },
        {
          category: 'On Demand',
          value: 31000,
          delta: 1300,
          change: '+',
        },
      ],
    },
    {
      title: 'Economy',
      type: 'money',
      data: [
        {
          category: 'Deal Maker',
          value: 100000,
          delta: 35000,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 80000,
          delta: 56200,
          change: '+',
        },
        {
          category: 'Executive',
          value: 80000,
          delta: 10000,
          change: '-',
        },
        {
          category: 'On Demand',
          value: 90000,
          delta: 13200,
          change: '-',
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

exports.routes = {
  airRoot: {
    title: 'Airline Tickets by Route Types',
    summary:
      'Us Domestic was the most frequently flown route type, accounting for 27% of the total tickets purchased in 2018. This was a 2% increase over 2017',
    label: 'All Routes',
    context: 'airRoot',
    total: 347,
    colors: ['#6fcfaf', '#86a6d6', '#b789d4', '#d67a7a', '#f7e9aa', '#75e0e2'],
    donutData: [
      {
        category: 'US Domestic',
        value: 43,
      },
      {
        category: 'Transpacific',
        value: 22,
      },
      {
        category: 'Intra Europe',
        value: 11,
      },
      {
        category: 'US MEA',
        value: 11,
      },
      {
        category: 'Intra Asia',
        value: 8,
      },
      {
        category: 'Transatlantic',
        value: 5,
        nextLevel: 'transatlantic',
      },
    ],
  },
  transatlantic: {
    title: 'Airline Tickets by Departure Countries',
    summary:
      'Among Transatlantic flights, the most popular departure country was the United States, at 35% of tickets. This was a decerease of 3% from 2017. The largest increase occured for France which saw a 25% increase from 8% of Transatlantic tickets in 2017 to 10% of Transatnaltic tickets in 2018.',
    label: 'Transatlantic',
    context: 'transatlantic',
    total: 125,
    colors: [
      '#016366',
      '#027073',
      '#018083',
      '#039396',
      '#06A5A8',
      '#05B1B4',
      '#16C0C3',
      '#2DD2D5',
      '#45DCDF',
      '#5AE7E9',
      '#79F3F4',
      '#9AFBFC',
      '#BFFBFC',
      '#DAFCFC',
    ],
    donutData: [
      {
        category: 'United States',
        value: 31,
        nextLevel: 'unitedStates',
      },
      {
        category: 'United Kingdom',
        value: 21,
      },
      {
        category: 'Germany',
        value: 14,
      },
      {
        category: 'France',
        value: 12,
      },
      {
        category: 'Norway',
        value: 11,
      },
      {
        category: 'Spain',
        value: 11,
      },
    ],
  },
  unitedStates: {
    title: 'Airline Tickets by Departure Airports',
    summary:
      'Among Transatlantic flights in the United States, the most popular departure airport was LAX, at 27% of tickets. This was a 7% increase over 2017. The largest increase occured with ATL, which saw a 10% increase from 20% of tickets in 2017 to 22% in 2018.',
    label: 'United States',
    total: 250,
    context: 'unitedStates',
    colors: [
      '#016366',
      '#027073',
      '#018083',
      '#039396',
      '#06A5A8',
      '#05B1B4',
      '#16C0C3',
      '#2DD2D5',
      '#45DCDF',
      '#5AE7E9',
      '#79F3F4',
      '#9AFBFC',
      '#BFFBFC',
      '#DAFCFC',
    ],
    donutData: [
      {
        category: 'ORD',
        value: 31,
      },
      {
        category: 'JFK',
        value: 21,
        nextLevel: 'jfk',
      },
      {
        category: 'ATL',
        value: 14,
      },
      {
        category: 'LAX',
        value: 12,
      },
      {
        category: 'DIA',
        value: 11,
      },
      {
        category: 'DFW',
        value: 11,
      },
    ],
  },
  jfk: {
    title: 'Airline Tickets by Arrivals',
    summary:
      'Among Transatlantic flights in the United States departing from JFK, the most popular airport destination was AMS, at 27% of tickets. This was a 7% increase over 2017. The largest occured with ATL, which saw a 10% increase from 20% of tickets in 2017 to 22% in 2018.',
    label: 'JFK',
    total: 50,
    context: 'jfk',
    colors: [
      '#016366',
      '#027073',
      '#018083',
      '#039396',
      '#06A5A8',
      '#05B1B4',
      '#16C0C3',
      '#2DD2D5',
      '#45DCDF',
      '#5AE7E9',
      '#79F3F4',
      '#9AFBFC',
      '#BFFBFC',
      '#DAFCFC',
    ],
    donutData: [
      {
        category: 'MUC',
        value: 31,
      },
      {
        category: 'CDG',
        value: 21,
      },
      {
        category: 'MAD',
        value: 14,
      },
      {
        category: 'FCO',
        value: 12,
      },
      {
        category: 'LON',
        value: 11,
      },
      {
        category: 'FRA',
        value: 11,
      },
    ],
  },
};
