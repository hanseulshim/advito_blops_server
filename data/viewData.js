exports.viewData = [
  {
    title: '360 analytics',
    icon: 'analytics_active.png',
    disabled: false,
    list: [
      {
        title: 'Travel Manager Dashboard',
        icon: 'manager_active.png',
        link: '/travel',
      },
      {
        title: 'Executive Dashboard',
        icon: 'manager_active.png',
        link: '/executive',
      },
      {
        title: 'Card Deck',
        icon: 'tool_active.png',
        domo: true,
        link: 'https://www.domo.com/',
      },
    ],
  },
  {
    title: 'air',
    icon: 'air_disabled.png',
    disabled: true,
    list: [
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
    icon: 'hotel_disabled.png',
    disabled: true,
    list: [
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

exports.infoData = [
  {
    title: 'Webinar Name',
    description: 'Information about webinar',
    icon: 'tool_disabled.png',
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
    icon: 'tool_disabled.png',
    disabled: true,
    button: 'download',
  },
];
