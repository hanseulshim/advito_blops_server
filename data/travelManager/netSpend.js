const spend = [
  {
    date: '2018-01-15',
    projSpend: 2300,
    actualSpend: 2100,
  },
  {
    date: '2018-02-15',
    projSpend: 2100,
    actualSpend: 1100,
  },
  {
    date: '2018-03-15',
    projSpend: 2600,
    actualSpend: 2400,
  },
  {
    date: '2018-04-15',
    projSpend: 1900,
    actualSpend: 1800,
  },
  {
    date: '2018-05-15',
    projSpend: 2100,
    actualSpend: 1900,
  },
  {
    date: '2018-06-15',
    projSpend: 2900,
    actualSpend: 2500,
  },
  {
    date: '2018-07-15',
    projSpend: 1800,
    actualSpend: 1700,
  },
  {
    date: '2018-08-15',
    projSpend: 2100,
    actualSpend: 1900,
  },
  {
    date: '2018-09-15',
    projSpend: 2200,
    actualSpend: 1500,
  },
  {
    date: '2018-10-15',
    projSpend: 2500,
    actualSpend: 2700,
  },
  {
    date: '2018-11-15',
    projSpend: 2300,
    actualSpend: 2500,
  },
  {
    date: '2018-12-15',
    projSpend: 2200,
    actualSpend: 2600,
  },
  {
    date: '2019-01-15',
    projSpend: 2000,
    actualSpend: 2500,
  },
].map(v => ({
  ...v,
  delta: Math.floor(((v.projSpend - v.actualSpend) / v.projSpend) * 100),
  color: v.projSpend > v.actualSpend ? '#4baaa3' : '#EB707F',
}));

exports.netSpend = {
  spendCategories: [
    {
      title: 'Ancillary',
      icon: 'icon_ancillary.png',
      amount: 200,
      diff: -0.3,
    },
    {
      title: 'Meals',
      icon: 'icon_meals.png',
      amount: 375,
      diff: -0.1,
    },
    {
      title: 'Travel',
      icon: 'tickets_icon.png',
      amount: 950,
      diff: -0.05,
    },
    {
      title: 'Lodging',
      icon: 'rooms_icon.png',
      amount: 1495,
      diff: 0.3,
    },
  ],
  spend,
  summary: {
    title: 'Lodging',
    info:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
  },
};
