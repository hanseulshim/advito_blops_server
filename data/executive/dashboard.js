exports.programPerformanceExecutive = {
  value: 7.1,
};

const netSpendAnalysisListExecutive = [];
for (let i = 1; i <= 15; i++) {
  netSpendAnalysisListExecutive.push({
    date: `2019-06-${i}`,
    value: Math.floor(Math.random() * 10 + i),
  });
}
exports.netSpendAnalysisListExecutive = netSpendAnalysisListExecutive;

exports.marketList = [
  {
    title: 'commercial',
    value: 5.7,
    programShare: 40,
  },
  {
    title: 'international',
    value: 3.8,
    programShare: 25,
  },
  {
    title: 'retail',
    value: 5.8,
    programShare: 15,
  },
  {
    title: 'corporate',
    value: 7.8,
    programShare: 10,
  },
];

exports.savingsOpportunityList = [
  {
    id: 1,
    title: 'Amount to incentive/Rebate (personal card)',
    value: '$150K',
    divisionList: [
      { title: 'it', value: '$11K' },
      { title: 'recruiting', value: '$3.1K' },
      { title: 'product', value: '$2.9K' },
    ],
  },
  {
    id: 2,
    title: 'Breakfast & Wifi Expensed',
    value: '$200K',
    divisionList: [
      { title: 'product', value: '$2.4K' },
      { title: 'security', value: '23', secondaryValue: '$2.4K' },
      { title: 'regulatory', value: '21', secondaryValue: '$1.7K' },
    ],
  },
  {
    id: 3,
    title: 'Actual vs negotiated save rate',
    value: '10%',
    secondaryValue: '8%',
    unit: 'Actual',
    secondaryUnit: 'Negotiated',
    divisionList: [
      { title: 'commercial sales', value: '5%', secondaryValue: '4%' },
      { title: 'international sales', value: '4%', secondaryValue: '2.5%' },
      { title: 'regulatory', value: '2%', secondaryValue: '1%' },
    ],
  },
  {
    id: 4,
    title: 'Volume of ancillary spend',
    value: '$800K',
    divisionList: [
      { title: 'product', value: '$140k' },
      { title: 'it', value: '$120k' },
      { title: 'security', value: '$50k' },
    ],
  },
  {
    id: 5,
    title: 'Contracted savings lost',
    value: '$200K',
    divisionList: [
      { title: 'international sales', value: '$15K' },
      { title: 'retail sales', value: '$12.5K' },
      { title: 'retail marketing', value: '$3.7K' },
    ],
  },
];

exports.riskAreaList = [
  {
    id: 1,
    title: 'T&E spend to forecasted budget value',
    value: '$3.2M',
    secondaryValue: '$3.5M',
    divisionList: [
      { title: 'regulatory', value: '$394K', secondaryValue: '$280K' },
      { title: 'security', value: '$327K', secondaryValue: '$300K' },
      { title: 'product', value: '$420K', secondaryValue: '$415K' },
    ],
  },
  {
    id: 2,
    title: 'Non-expensed trips (days since trip)',
    value: '21',
    secondaryValue: '$150K',
    divisionList: [
      { title: 'retail sales', value: '32', secondaryValue: '$24K' },
      { title: 'it', value: '23', secondaryValue: '$18K' },
      { title: 'international sales', value: '15', secondaryValue: '$32K' },
    ],
  },
  {
    id: 3,
    title: 'Past due corporate cards',
    value: '21%',
    secondaryValue: '$98K',
    divisionList: [
      { title: 'it', value: '26%', secondaryValue: '$15K' },
      { title: 'commercial sales', value: '19%', secondaryValue: '$12K' },
      { title: 'retail marketing', value: '16%', secondaryValue: '$8K' },
    ],
  },
  {
    id: 4,
    title: 'Time away/employee burn out',
    value: '34%',
    divisionList: [
      { title: 'commercial sales', value: '42%' },
      { title: 'international sales', value: '38%' },
      { title: 'regulatory', value: '18%' },
    ],
  },
  {
    id: 5,
    title: 'Approved out of policy spend',
    value: '$472K',
    divisionList: [
      { title: 'international sales', value: '$123K' },
      { title: 'retail sales', value: '$52K' },
      { title: 'recruiting', value: '$27K' },
    ],
  },
];
