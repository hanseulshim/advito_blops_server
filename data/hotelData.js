exports.hotelSummary = {
  title: 'Hotel Summary',
  summary:
    '2017 was a busy year. Your company flew 3.18M miles, or 6.1M km between 12 countries. Deal makers comprised of the most spend and miles traveled, while Executives saved the most.',
  kpis: [
    {
      title: 'Spend',
      value: 52400000,
      delta: 1200000,
      change: '-',
      type: 'money',
      icon: 'spend_icon.png',
    },
    {
      title: 'Room Nights',
      value: 132000,
      delta: 4100,
      change: '+',
      type: '',
      icon: 'rooms_icon.png',
    },
    {
      title: 'Cities Visited',
      value: 27,
      delta: 2,
      change: '+',
      type: '',
      icon: 'cities_icon.png',
    },
    {
      title: 'Hotels Stayed',
      value: 133,
      delta: 14,
      change: '+',
      type: '',
      icon: 'hotels_icon.png',
    },
    {
      title: 'Savings',
      value: 64000,
      delta: 4900,
      change: '+',
      type: '',
      icon: 'savings_icon.png',
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
      title: 'Room Nights',
      type: '',
      data: [
        {
          category: 'Deal Maker',
          value: 10000,
          delta: 1200,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 8000,
          delta: 4800,
          change: '+',
        },
        {
          category: 'Executive',
          value: 7000,
          delta: 1900,
          change: '+',
        },
        {
          category: 'On Demand',
          value: 9000,
          delta: 961,
          change: '-',
        },
      ],
    },
    {
      title: 'Cities Visited',
      type: '',
      data: [
        {
          category: 'Deal Maker',
          value: 5,
          delta: 1,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 4,
          delta: 2,
          change: '-',
        },
        {
          category: 'Executive',
          value: 6,
          delta: 2,
          change: '+',
        },
        {
          category: 'On Demand',
          value: 5,
          delta: 3,
          change: '-',
        },
      ],
    },
    {
      title: 'Hotels Stayed',
      type: '',
      data: [
        {
          category: 'Deal Maker',
          value: 50,
          delta: 14,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 45,
          delta: 6,
          change: '+',
        },
        {
          category: 'Executive',
          value: 45,
          delta: 2,
          change: '-',
        },
        {
          category: 'On Demand',
          value: 50,
          delta: 12,
          change: '-',
        },
      ],
    },
    {
      title: 'Savings',
      type: '',
      data: [
        {
          category: 'Deal Maker',
          value: 10000,
          delta: 4400,
          change: '+',
        },
        {
          category: 'Road Warrior',
          value: 9000,
          delta: 1500,
          change: '+',
        },
        {
          category: 'Executive',
          value: 9000,
          delta: 1100,
          change: '-',
        },
        {
          category: 'On Demand',
          value: 10000,
          delta: 900,
          change: '-',
        },
      ],
    },
  ],
  locations: [
    {
      title: 'Vienna',
      radius: Math.floor(Math.random() * 15) + 5,
      latitude: 48.2092,
      longitude: 16.3728,
    },
    {
      title: 'Minsk',
      radius: Math.floor(Math.random() * 15) + 5,
      latitude: 53.9678,
      longitude: 27.5766,
    },
    {
      title: 'Brussels',
      radius: Math.floor(Math.random() * 15) + 5,
      latitude: 50.8371,
      longitude: 4.3676,
    },
    {
      title: 'Sarajevo',
      radius: Math.floor(Math.random() * 15) + 5,
      latitude: 43.8608,
      longitude: 18.4214,
    },
    {
      title: 'Sofia',
      radius: Math.floor(Math.random() * 15) + 5,
      latitude: 42.7105,
      longitude: 23.3238,
    },
    {
      title: 'Zagreb',
      radius: Math.floor(Math.random() * 15) + 5,
      latitude: 45.815,
      longitude: 15.9785,
    },
    {
      title: 'Pristina',
      radius: Math.floor(Math.random() * 15) + 5,
      latitude: 42.666667,
      longitude: 21.166667,
    },
    {
      title: 'Prague',
      radius: Math.floor(Math.random() * 15) + 5,
      latitude: 50.0878,
      longitude: 14.4205,
    },
    {
      title: 'Copenhagen',
      radius: Math.floor(Math.random() * 15) + 5,
      latitude: 55.6763,
      longitude: 12.5681,
    },
    {
      title: 'Tallinn',
      radius: Math.floor(Math.random() * 15) + 5,
      latitude: 59.4389,
      longitude: 24.7545,
    },
    {
      title: 'Helsinki',
      radius: Math.floor(Math.random() * 15) + 5,
      latitude: 60.1699,
      longitude: 24.9384,
    },
    {
      title: 'Paris',
      radius: Math.floor(Math.random() * 15) + 5,
      latitude: 48.8567,
      longitude: 2.351,
    },
    {
      title: 'Berlin',
      radius: Math.floor(Math.random() * 15) + 5,
      latitude: 52.5235,
      longitude: 13.4115,
    },
  ],
};

exports.hotelSpend = {
  title: 'Hotel Spend by Top Countries',
  summary:
    'The country with the highest spend was United States, at $16.1M. It also saw the most savings and most room nights',
  kpis: [
    {
      title: 'United States',
      value: 16100000,
      delta: 411000,
      change: '-',
      type: 'money',
      icon: 'countries_icon.png',
    },
    {
      title: 'Spain',
      value: 12800000,
      delta: 56000,
      change: '+',
      type: 'money',
      icon: 'countries_icon.png',
    },
    {
      title: 'United Kingdom',
      value: 10000000,
      delta: 306000,
      change: '-',
      type: 'money',
      icon: 'countries_icon.png',
    },
    {
      title: 'China',
      value: 9400000,
      delta: 312000,
      change: '-',
      type: 'money',
      icon: 'countries_icon.png',
    },
    {
      title: 'France',
      value: 8900000,
      delta: 178000,
      change: '-',
      type: 'money',
      icon: 'countries_icon.png',
    },
    {
      title: 'Germany',
      value: 2200000,
      delta: 41000,
      change: '-',
      type: 'money',
      icon: 'countries_icon.png',
    },
  ],
  barchart: [
    {
      title: 'Spend',
      type: 'money',
      data: [
        {
          category: 'United States',
          value: 50000,
          delta: 25000,
          change: '+',
        },
        {
          category: 'Spain',
          value: 40000,
          delta: 12000,
          change: '+',
        },
        {
          category: 'United Kingdom',
          value: 45000,
          delta: 10000,
          change: '+',
        },
        {
          category: 'China',
          value: 30000,
          delta: 9200,
          change: '+',
        },
        {
          category: 'France',
          value: 35000,
          delta: 6100,
          change: '+',
        },
        {
          category: 'Germany',
          value: 30000,
          delta: 4000,
          change: '+',
        },
      ],
    },
    {
      title: 'Room Nights',
      type: '',
      data: [
        {
          category: 'United States',
          value: 100,
          delta: 402,
          change: '+',
        },
        {
          category: 'Spain',
          value: 80,
          delta: 54,
          change: '-',
        },
        {
          category: 'United Kingdom',
          value: 75,
          delta: 89,
          change: '+',
        },
        {
          category: 'China',
          value: 85,
          delta: 46,
          change: '-',
        },
        {
          category: 'France',
          value: 80,
          delta: 43,
          change: '+',
        },
        {
          category: 'Germany',
          value: 85,
          delta: 28,
          change: '+',
        },
      ],
    },
    {
      title: 'Cities Visited',
      type: '',
      data: [
        {
          category: 'United States',
          value: 5000,
          delta: 4400,
          change: '+',
        },
        {
          category: 'Spain',
          value: 5500,
          delta: 1500,
          change: '+',
        },
        {
          category: 'United Kingdom',
          value: 4500,
          delta: 1100,
          change: '+',
        },
        {
          category: 'China',
          value: 4500,
          delta: 900,
          change: '-',
        },
        {
          category: 'France',
          value: 4000,
          delta: 650,
          change: '+',
        },
        {
          category: 'Germany',
          value: 5000,
          delta: 450,
          change: '+',
        },
      ],
    },
    {
      title: 'Hotels Stayed',
      type: '',
      data: [
        {
          category: 'United States',
          value: 18.5,
          delta: 18.5,
          change: '+',
        },
        {
          category: 'Spain',
          value: 16.2,
          delta: 12.2,
          change: '+',
        },
        {
          category: 'United Kingdom',
          value: 17.1,
          delta: 10.1,
          change: '+',
        },
        {
          category: 'China',
          value: 15.96,
          delta: 5.96,
          change: '-',
        },
        {
          category: 'France',
          value: 16.25,
          delta: 1.25,
          change: '+',
        },
        {
          category: 'Germany',
          value: 14.59,
          delta: 0.59,
          change: '+',
        },
      ],
    },
    {
      title: 'Savings',
      type: 'money',
      data: [
        {
          category: 'United States',
          value: 18.5,
          delta: 18.5,
          change: '+',
        },
        {
          category: 'Spain',
          value: 16.2,
          delta: 12.2,
          change: '+',
        },
        {
          category: 'United Kingdom',
          value: 17.1,
          delta: 10.1,
          change: '+',
        },
        {
          category: 'China',
          value: 15.96,
          delta: 5.96,
          change: '-',
        },
        {
          category: 'France',
          value: 16.25,
          delta: 1.25,
          change: '+',
        },
        {
          category: 'Germany',
          value: 14.59,
          delta: 0.59,
          change: '+',
        },
      ],
    },
  ],
  locations: [
    {
      title: 'Belmopan',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 17.2534,
      longitude: -88.7713,
    },
    {
      title: 'Sucre',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: -19.0421,
      longitude: -65.2559,
    },
    {
      title: 'Brasilia',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: -15.7801,
      longitude: -47.9292,
    },
    {
      title: 'Ottawa',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 45.4235,
      longitude: -75.6979,
    },
    {
      title: 'Santiago',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: -33.4691,
      longitude: -70.642,
    },
    {
      title: 'Bogota',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 4.6473,
      longitude: -74.0962,
    },
    {
      title: 'San Jose',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 9.9402,
      longitude: -84.1002,
    },
    {
      title: 'Havana',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 23.1333,
      longitude: -82.3667,
    },
    {
      title: 'Roseau',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 15.2976,
      longitude: -61.39,
    },
    {
      title: 'Santo Domingo',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 18.479,
      longitude: -69.8908,
    },
    {
      title: 'Quito',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: -0.2295,
      longitude: -78.5243,
    },
    {
      title: 'San Salvador',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 13.7034,
      longitude: -89.2073,
    },
    {
      title: 'Guatemala',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 14.6248,
      longitude: -90.5328,
    },
    {
      title: 'Ciudad de Mexico',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 19.4271,
      longitude: -99.1276,
    },
    {
      title: 'Managua',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 12.1475,
      longitude: -86.2734,
    },
    {
      title: 'Panama',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 8.9943,
      longitude: -79.5188,
    },
    {
      title: 'Asuncion',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: -25.3005,
      longitude: -57.6362,
    },
    {
      title: 'Lima',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: -12.0931,
      longitude: -77.0465,
    },
    {
      title: 'Castries',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 13.9972,
      longitude: -60.0018,
    },
    {
      title: 'Paramaribo',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 5.8232,
      longitude: -55.1679,
    },
    {
      title: 'Washington D.C.',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 38.8921,
      longitude: -77.0241,
    },
    {
      title: 'Montevideo',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: -34.8941,
      longitude: -56.0675,
    },
    {
      title: 'Caracas',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 10.4961,
      longitude: -66.8983,
    },
    {
      title: 'Oranjestad',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 12.5246,
      longitude: -70.0265,
    },
    {
      title: 'Cayenne',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 4.9346,
      longitude: -52.3303,
    },
    {
      title: 'Plymouth',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 16.6802,
      longitude: -62.2014,
    },
    {
      title: 'San Juan',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 18.45,
      longitude: -66.0667,
    },
    {
      title: 'Algiers',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 36.7755,
      longitude: 3.0597,
    },
    {
      title: 'Luanda',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: -8.8159,
      longitude: 13.2306,
    },
    {
      title: 'Porto-Novo',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 6.4779,
      longitude: 2.6323,
    },
    {
      title: 'Gaborone',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: -24.657,
      longitude: 25.9089,
    },
    {
      title: 'Ouagadougou',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: 12.3569,
      longitude: -1.5352,
    },
    {
      title: 'Bujumbura',
      radius: Math.floor(Math.random() * 20) + 20,
      latitude: -3.3818,
      longitude: 29.3622,
    },
  ],
};

exports.topHotelChains = {
  title: 'Top Hotel Chains',
  summary:
    'The top hotel chain by net effective savings ratio was Marriot at 18.1%. The hotel chain that saw the largest increase in net effective savings ratio was Hilton while the hotel chain that saw the largest decrease was Holiday Inn.',
  categories: [
    {
      title: 'Spend',
      type: 'money',
      icon: 'spend_icon.png',
      total: 39.2,
      subCategories: [
        {
          name: 'Marriott',
          value: 12,
          color: '#8DC6e7',
        },
        {
          name: 'Hilton',
          value: 6.6,
          color: '#468ab2',
        },
        {
          name: 'Hyatt',
          value: 2.1,
          color: '#085887',
        },
        {
          name: 'Holiday Inn',
          value: 7.8,
          color: '#032f56',
        },
        {
          name: 'DoubleTree',
          value: 9,
          color: '#032f56',
        },
        {
          name: 'Other',
          value: 1.7,
          color: '#032f56',
        },
      ],
    },
    {
      title: 'Room Nights',
      icon: 'rooms_icon.png',
      total: 99,
      subCategories: [
        {
          name: 'Marriott',
          value: 30.3,
          color: '#8DC6e7',
        },
        {
          name: 'Hilton',
          value: 22.8,
          color: '#468ab2',
        },
        {
          name: 'Hyatt',
          value: 19.7,
          color: '#085887',
        },
        {
          name: 'Holiday Inn',
          value: 16.7,
          color: '#032f56',
        },
        {
          name: 'DoubleTree',
          value: 5.3,
          color: '#032f56',
        },
        {
          name: 'Other',
          value: 4.2,
          color: '#032f56',
        },
      ],
    },
    {
      title: 'Savings',
      icon: 'savings_icon.png',
      total: 3916000,
      subCategories: [
        {
          name: 'Marriott',
          value: 1100000,
          color: '#8DC6e7',
        },
        {
          name: 'Hilton',
          value: 1000000,
          color: '#468ab2',
        },
        {
          name: 'Hyatt',
          value: 295000,
          color: '#085887',
        },
        {
          name: 'Holiday Inn',
          value: 771000,
          color: '#032f56',
        },
        {
          name: 'DoubleTree',
          value: 460000,
          color: '#032f56',
        },
        {
          name: 'Other',
          value: 290000,
          color: '#032f56',
        },
      ],
    },
  ],
  barchart: [
    {
      title: 'Spend',
      type: 'money',
      data: [
        {
          category: 'Marriott',
          value: 30000,
          delta: 14200,
          change: '+',
        },
        {
          category: 'Holiday Inn',
          value: 28000,
          delta: 13900,
          change: '+',
        },
        {
          category: 'Hilton',
          value: 30000,
          delta: 200,
          change: '+',
        },
        {
          category: 'Doubletree',
          value: 25000,
          delta: 11000,
          change: '+',
        },
        {
          category: 'Hyatt',
          value: 30000,
          delta: 2500,
          change: '+',
        },
        {
          category: 'Other',
          value: 27000,
          delta: 1600,
          change: '+',
        },
      ],
    },
    {
      title: 'Room Nights',
      type: '',
      data: [
        {
          category: 'Marriott',
          value: 50,
          delta: 26,
          change: '+',
        },
        {
          category: 'Holiday Inn',
          value: 30,
          delta: 20,
          change: '-',
        },
        {
          category: 'Hilton',
          value: 25,
          delta: 22,
          change: '+',
        },
        {
          category: 'Doubletree',
          value: 45,
          delta: 14,
          change: '-',
        },
        {
          category: 'Hyatt',
          value: 40,
          delta: 9,
          change: '+',
        },
        {
          category: 'Other',
          value: 45,
          delta: 9,
          change: '+',
        },
      ],
    },
    {
      title: 'Hotels Stayed',
      type: '',
      data: [
        {
          category: 'Marriott',
          value: 50,
          delta: 14,
          change: '+',
        },
        {
          category: 'Holiday Inn',
          value: 45,
          delta: 6,
          change: '-',
        },
        {
          category: 'Hilton',
          value: 55,
          delta: 20,
          change: '+',
        },
        {
          category: 'Doubletree',
          value: 50,
          delta: 3,
          change: '+',
        },
        {
          category: 'Hyatt',
          value: 55,
          delta: 1,
          change: '+',
        },
        {
          category: 'Other',
          value: 40,
          change: '',
        },
      ],
    },
    {
      title: 'Savings',
      type: 'money',
      data: [
        {
          category: 'Marriott',
          value: 10000,
          delta: 4200,
          change: '+',
        },
        {
          category: 'Holiday Inn',
          value: 9000,
          delta: 3900,
          change: '+',
        },
        {
          category: 'Hilton',
          value: 12000,
          delta: 1200,
          change: '+',
        },
        {
          category: 'Doubletree',
          value: 9500,
          delta: 1000,
          change: '-',
        },
        {
          category: 'Hyatt',
          value: 10000,
          delta: 270,
          change: '+',
        },
        {
          category: 'Other',
          value: 9000,
          delta: 960,
          change: '+',
        },
      ],
    },
    {
      title: 'Net Effective Savings Ratio',
      type: 'percent',
      data: [
        {
          category: 'Marriott',
          value: 0.6,
          delta: 0.42,
          change: '+',
        },
        {
          category: 'Holiday Inn',
          value: 0.8,
          delta: 0.35,
          change: '+',
        },
        {
          category: 'Hilton',
          value: 0.4,
          delta: 0.15,
          change: '+',
        },
        {
          category: 'Doubletree',
          value: 0.6,
          delta: 0.05,
          change: '-',
        },
        {
          category: 'Hyatt',
          value: 0.4,
          delta: 0.03,
          change: '-',
        },
        {
          category: 'Other',
          value: 0.5,
          delta: 0.02,
          change: '-',
        },
      ],
    },
  ],
};

exports.topHotelTiers = {
  title: 'Top Hotel Tiers',
  summary:
    'The most popular hotel tier in 2017 was Luxury, with a spend of $20.4M (38.3K room nights) and $3.3M in savings. This was the largest increase from last year, at 8%.',
  categories: [
    {
      title: 'Spend',
      type: 'money',
      icon: 'spend_icon.png',
      total: 51900000,
      subCategories: [
        {
          name: 'Luxury',
          value: 20000000,
          color: '#8DC6e7',
        },
        {
          name: 'Upscale',
          value: 8400000,
          color: '#468ab2',
        },
        {
          name: 'Budget',
          value: 1000000,
          color: '#085887',
        },
        {
          name: 'Upper Upscale',
          value: 13600000,
          color: '#032f56',
        },
        {
          name: 'Midscale',
          value: 8900000,
          color: '#032f56',
        },
      ],
    },
    {
      title: 'Room Nights',
      type: '',
      icon: 'rooms_icon.png',
      total: 122000,
      subCategories: [
        {
          name: 'Luxury',
          value: 38300,
          color: '#8DC6e7',
        },
        {
          name: 'Upscale',
          value: 25100,
          color: '#468ab2',
        },
        {
          name: 'Budget',
          value: 11900,
          color: '#085887',
        },
        {
          name: 'Upper Upscale',
          value: 25600,
          color: '#032f56',
        },
        {
          name: 'Midscale',
          value: 21100,
          color: '#032f56',
        },
      ],
    },
    {
      title: 'Savings',
      type: 'money',
      icon: 'savings_icon.png',
      total: 6300000,
      subCategories: [
        {
          name: 'Luxury',
          value: 3300000,
          color: '#8DC6e7',
        },
        {
          name: 'Upscale',
          value: 400000,
          color: '#468ab2',
        },
        {
          name: 'Budget',
          value: 100000,
          color: '#085887',
        },
        {
          name: 'Upper Upscale',
          value: 1900000,
          color: '#032f56',
        },
        {
          name: 'Midscale',
          value: 600000,
          color: '#032f56',
        },
      ],
    },
  ],
  barchart: [
    {
      title: 'Spend',
      type: 'money',
      data: [
        {
          category: 'Luxury',
          value: 30000,
          delta: 14200,
          change: '+',
        },
        {
          category: 'Upper Upscale',
          value: 28000,
          delta: 13900,
          change: '+',
        },
        {
          category: 'Upscale',
          value: 30000,
          delta: 200,
          change: '+',
        },
        {
          category: 'Midscale',
          value: 25000,
          delta: 11000,
          change: '+',
        },
        {
          category: 'Budget',
          value: 30000,
          delta: 2500,
          change: '+',
        },
      ],
    },
    {
      title: 'Room Nights',
      type: '',
      data: [
        {
          category: 'Luxury',
          value: 50,
          delta: 26,
          change: '+',
        },
        {
          category: 'Upper Upscale',
          value: 30,
          delta: 20,
          change: '-',
        },
        {
          category: 'Upscale',
          value: 25,
          delta: 22,
          change: '+',
        },
        {
          category: 'Midscale',
          value: 45,
          delta: 14,
          change: '-',
        },
        {
          category: 'Budget',
          value: 40,
          delta: 9,
          change: '+',
        },
      ],
    },
    {
      title: 'Avg Room Rate',
      type: 'money',
      data: [
        {
          category: 'Luxury',
          value: 50,
          delta: 14,
          change: '+',
        },
        {
          category: 'Upper Upscale',
          value: 45,
          delta: 6,
          change: '-',
        },
        {
          category: 'Upscale',
          value: 55,
          delta: 20,
          change: '+',
        },
        {
          category: 'Midscale',
          value: 50,
          delta: 3,
          change: '+',
        },
        {
          category: 'Budget',
          value: 55,
          delta: 1,
          change: '+',
        },
      ],
    },
    {
      title: 'Savings',
      type: 'money',
      data: [
        {
          category: 'Luxury',
          value: 10000,
          delta: 4200,
          change: '+',
        },
        {
          category: 'Upper Upscale',
          value: 9000,
          delta: 3900,
          change: '+',
        },
        {
          category: 'Upscale',
          value: 12000,
          delta: 1200,
          change: '+',
        },
        {
          category: 'Midscale',
          value: 9500,
          delta: 1000,
          change: '-',
        },
        {
          category: 'Budget',
          value: 10000,
          delta: 270,
          change: '+',
        },
      ],
    },
    {
      title: 'Net Effective Savings Ratio',
      type: 'percent',
      data: [
        {
          category: 'Luxury',
          value: 0.6,
          delta: 0.42,
          change: '+',
        },
        {
          category: 'Upper Upscale',
          value: 0.8,
          delta: 0.35,
          change: '+',
        },
        {
          category: 'Upscale',
          value: 0.55,
          delta: 0.15,
          change: '+',
        },
        {
          category: 'Midscale',
          value: 0.3,
          delta: 0.05,
          change: '-',
        },
        {
          category: 'Budget',
          value: 0.4,
          delta: 0.03,
          change: '-',
        },
      ],
    },
  ],
};

exports.roomNights = {
  hotelRoot: {
    title: 'Room Nights by City',
    summary:
      'Among hotels in the UK, the city with the most room nights was London, with 16.9K room nights. This was a 11% increase over 2016. The largest increase occured with Glasgow, which saw a 12% increase from 4.3K of UK room nights in 2016 to 4.8K in 2017',
    label: 'All Regions',
    context: 'hotelRoot',
    total: 132000,
    colors: ['#6fcfaf', '#86a6d6', '#b789d4', '#d67a7a', '#f7e9aa', '#75e0e2'],
    donutData: [
      {
        category: 'North America',
        value: 40600,
      },
      {
        category: 'Europe',
        value: 26200,
        nextLevel: 'europe',
      },
      {
        category: 'Asia Pacific',
        value: 65200,
      },
    ],
  },
  europe: {
    title: 'Room Nights by Country',
    summary:
      'Among hotels in Europe, the country witht he most room nights was the UK, at 30.2K room nights. THis was a decrease of 2% from 2016. The largest increase occured for France which saw a 19% increase, from 18.8K of Europe room nights in 2016 to 22.4K of Europe room nights in 2017.',
    label: 'Europe',
    context: 'europe',
    total: 65200,
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
        category: 'United Kingdom',
        value: 30200,
        nextLevel: 'unitedKingdom',
      },
      {
        category: 'Germany',
        value: 22400,
      },
      {
        category: 'France',
        value: 7100,
      },
      {
        category: 'Spain',
        value: 5500,
      },
    ],
  },
  unitedKingdom: {
    title: 'Room Nights by City',
    summary:
      'Among hotels in the UK, the city with the most room nights was London, with 16.9K room nights. THis was a 11% increase over 2016. The largest increase occured with Glasgow, which saw a 12% increase from 4.3K of UK room nights in 2016 to 4.8K in 2017.',
    label: 'United Kingdom',
    total: 31300,
    context: 'unitedKingdom',
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
        category: 'London',
        value: 16900,
      },
      {
        category: 'Glasgow',
        value: 4800,
      },
      {
        category: 'Edinburgh',
        value: 3600,
      },
      {
        category: 'Birmingham',
        value: 1800,
      },
      {
        category: 'Liverpool',
        value: 1900,
      },
      {
        category: 'Manchester',
        value: 1800,
      },
      {
        category: 'Bristol',
        value: 500,
      },
    ],
  },
};
