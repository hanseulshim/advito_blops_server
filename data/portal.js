exports.upcomingActionList = [
  {
    header: 'April 31, 2019',
    secondaryHeader: '2nd Round Hotel Negotiations Due',
    icon: 'flag.png',
    alert: false,
  },
  {
    header: 'May 13, 2019',
    secondaryHeader: 'Hotel Audits Due',
    icon: 'flag.png',
    alert: false,
  },
  {
    header: 'May 29, 2019',
    secondaryHeader: 'Delta Contract Expires',
    icon: 'contracts.png',
    alert: false,
  },
];

exports.activeAlertList = [
  {
    header: '',
    secondaryHeader: 'Leakage to Program',
    icon: 'air.png',
    alert: true,
  },
  {
    header: '',
    secondaryHeader: 'Performance against target',
    icon: 'air.png',
    alert: true,
  },
  {
    header: '',
    secondaryHeader: 'Performance against target',
    icon: 'hotel.png',
    alert: true,
  },
  {
    header: '',
    secondaryHeader: 'ATP to ancillary spend',
    icon: 'air.png',
    alert: true,
  },
];

exports.productList = [
  {
    title: '360 analytics',
    icon: '360_console.png',
    disabled: false,
    optionList: [
      {
        title: 'Travel Manager Dashboard',
        icon: 'manager_active.png',
        link: '/travel/dashboard',
      },
      {
        title: 'Executive Dashboard',
        icon: 'manager_active.png',
        link: '/executive/dashboard',
      },
      {
        title: 'Card Deck',
        icon: 'domo_active.png',
        domo: true,
        link: 'https://www.domo.com/',
      },
    ],
  },
  {
    title: 'air',
    icon: 'air_console.png',
    disabled: true,
    optionList: [
      {
        title: 'Air program analytics',
        icon: 'manager_disabled.png',
        link: '#',
      },
      {
        title: 'Air program manager (A3)',
        icon: 'tool_disabled.png',
        link: '#',
      },
    ],
  },
  {
    title: 'hotel',
    icon: 'hotel_console.png',
    disabled: true,
    optionList: [
      {
        title: 'Hotel program analytics',
        icon: 'manager_disabled.png',
        link: '#',
      },
      {
        title: 'Hotel program manager (HPM)',
        icon: 'tool_disabled.png',
        link: '#',
      },
    ],
  },
];

exports.productEventList = [
  {
    title: 'Webinar Name',
    description: 'Information about webinar',
    icon: 'webinar_disabled.png',
    disabled: true,
    button: 'register',
  },
  {
    title: 'Document Library',
    description: 'Information about library',
    icon: 'library_active.png',
    disabled: false,
    button: null,
  },
  {
    title: 'Podcast',
    description: 'Information about podcast',
    icon: 'podcast_disabled.png',
    disabled: true,
    button: 'download',
  },
  {
    title: 'Item Name',
    description: 'Information about item',
    icon: 'item_disabled.png',
    disabled: true,
    button: 'download',
  },
];
