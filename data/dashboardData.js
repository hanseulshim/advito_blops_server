exports.programPerformanceTravel = [
  {
    title: 'Average Total Trip Cost',
    value: '$2,754',
    unit: '',
  },
  {
    title: 'Booking Outside of Agency',
    value: '12% / $360K',
    unit: 'impact',
  },
  {
    title: 'Expenses Out of Policy',
    value: '23% / $690K',
    unit: 'impact',
  },
]

const netSpendAnalysisTravel = []
const netSpendAnalysisExecutive = []
for (let i = 1; i <= 15; i++) {
  netSpendAnalysisTravel.push({
    date: `2019-01-${i}`,
    value: Math.floor(Math.random() * 10 + i),
  })
  netSpendAnalysisExecutive.push({
    date: `2019-06-${i}`,
    value: Math.floor(Math.random() * 10 + i),
  })
}

exports.netSpendAnalysisTravel = netSpendAnalysisTravel
exports.netSpendAnalysisExecutive = netSpendAnalysisExecutive

exports.programPerformanceExecutive = {
  value: 7.1,
}

exports.noChangeSince = 'July 30'

exports.personaList = [
  {
    title: 'road warrior',
    value: '$3,350',
    programShare: 25,
  },
  {
    title: 'executive',
    value: '$3,150',
    programShare: 40,
  },
  {
    title: 'deal maker',
    value: '$2,561',
    programShare: 15,
  },
  {
    title: 'on demand',
    value: '$1,955',
    programShare: 10,
  },
]

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
]

exports.opportunitiesTravel = [
  {
    id: 1,
    title: 'Expenses approved above rate caps / per diems',
    value: '27%',
    secondaryValue: '$375K',
    secondaryUnit: 'impact',
  },
  {
    id: 2,
    title: 'ABR higher than ANR',
    value: '30%',
    secondaryValue: '$500k',
    secondaryUnit: 'impact',
  },
  {
    id: 3,
    title: 'NRT Utilization/Loss',
    value: '83%',
    secondaryValue: '$23k',
    secondaryUnit: 'expired',
  },
  {
    id: 4,
    title: 'ANR higher than ABR',
    value: '25% / $100K',
    unit: 'expired',
  },
  { id: 5, title: 'New item', value: 'XX% / $XX', unit: 'impact' },
  { id: 6, title: 'New item', value: 'XX% / $XX', unit: 'expired' },
  { id: 7, title: 'New item', value: 'XX% / $XX', unit: '' },
]

exports.opportunitiesExecutive = [
  {
    title: 'Amount to incentive/Rebate (personal card)',
    value: '$150K',
    divisions: [
      { title: 'it', value: '$11K' },
      { title: 'recruiting', value: '$3.1K' },
      { title: 'product', value: '$2.9K' },
    ],
  },
  {
    title: 'Breakfast & Wifi Expensed',
    value: '$200K',
    divisions: [
      { title: 'product', value: '$2.4K' },
      { title: 'security', value: '23', secondaryValue: '$2.4K' },
      { title: 'regulatory', value: '21', secondaryValue: '$1.7K' },
    ],
  },
  {
    title: 'Actual vs negotiated save rate',
    value: '10%',
    secondaryValue: '8%',
    unit: 'Actual',
    secondaryUnit: 'Negotiated',
    divisions: [
      { title: 'commercial sales', value: '5%', secondaryValue: '4%' },
      { title: 'international sales', value: '4%', secondaryValue: '2.5%' },
      { title: 'regulatory', value: '2%', secondaryValue: '1%' },
    ],
  },
  {
    title: 'Volume of ancillary spend',
    value: '$800K',
    divisions: [
      { title: 'product', value: '$140k' },
      { title: 'it', value: '$120k' },
      { title: 'security', value: '$50k' },
    ],
  },
  {
    title: 'Contracted savings lost',
    value: '$200K',
    divisions: [
      { title: 'international sales', value: '$15K' },
      { title: 'retail sales', value: '$12.5K' },
      { title: 'retail marketing', value: '$3.7K' },
    ],
  },
]

exports.riskAreasTravel = [
  {
    id: 1,
    title: 'Number of markets with ATP change more than 15%',
    value: '10',
  },
  {
    id: 2,
    title: 'Number of markets with rate availability lower than 80%',
    value: '14',
  },
  { id: 3, title: 'Travelers in HRC/Markets', value: '512' },
  { id: 4, title: 'Hosts in TBS/Markets', value: '125' },
  { id: 5, title: 'New item', value: 'XXX' },
  { id: 6, title: 'New item', value: 'XXX' },
  { id: 7, title: 'New item', value: 'XXX' },
]

exports.riskAreasExecutive = [
  {
    title: 'T&E spend to forecasted budget value',
    value: '$3.2M',
    secondaryValue: '$3.5M',
    divisions: [
      { title: 'regulatory', value: '$394K', secondaryValue: '$280K' },
      { title: 'security', value: '$327K', secondaryValue: '$300K' },
      { title: 'product', value: '$420K', secondaryValue: '$415K' },
    ],
  },
  {
    title: 'Non-expensed trips (days since trip)',
    value: '21',
    secondaryValue: '$150K',
    divisions: [
      { title: 'retail sales', value: '32', secondaryValue: '$24K' },
      { title: 'it', value: '23', secondaryValue: '$18K' },
      { title: 'international sales', value: '15', secondaryValue: '$32K' },
    ],
  },
  {
    title: 'Past due corporate cards',
    value: '21%',
    secondaryValue: '$98K',
    divisions: [
      { title: 'it', value: '26%', secondaryValue: '$15K' },
      { title: 'commercial sales', value: '19%', secondaryValue: '$12K' },
      { title: 'retail marketing', value: '16%', secondaryValue: '$8K' },
    ],
  },
  {
    title: 'Time away/employee burn out',
    value: '34%',
    divisions: [
      { title: 'commercial sales', value: '42%' },
      { title: 'international sales', value: '38%' },
      { title: 'regulatory', value: '18%' },
    ],
  },
  {
    title: 'Approved out of policy spend',
    value: '$472K',
    divisions: [
      { title: 'international sales', value: '$123K' },
      { title: 'retail sales', value: '$52K' },
      { title: 'recruiting', value: '$27K' },
    ],
  },
]
