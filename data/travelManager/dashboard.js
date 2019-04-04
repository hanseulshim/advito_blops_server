exports.programPerformanceListTravel = [
  {
    id: 1,
    title: 'Average Total Trip Cost',
    value: '$2,754',
    unit: '',
  },
  {
    id: 2,
    title: 'Booking Outside of Agency',
    value: '12% / $360K',
    unit: 'impact',
  },
  {
    id: 3,
    title: 'Expenses Out of Policy',
    value: '23% / $690K',
    unit: 'impact',
  },
];

const netSpendAnalysisListTravel = [];
for (let i = 1; i <= 15; i++) {
  netSpendAnalysisListTravel.push({
    date: `2019-01-${i}`,
    value: Math.floor(Math.random() * 10 + i),
  });
}

exports.netSpendAnalysisListTravel = netSpendAnalysisListTravel;

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
];

exports.savingsOpportunityList = [
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
];

exports.riskAreaList = [
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
];

exports.noChangeSince = 'July 30';
