const { savingsOpportunities } = require('../../../data/travelManager/savingsOpportunity');
const { riskAreas } = require('../../../data/travelManager/riskArea');
const { netSpend } = require('../../../data/travelManager/netSpend');
const { teBreakdown } = require('../../../data/travelManager/teBreakdown');

exports.categoryQueries = {
  savingsOpportunityDetail: (_, payload) => savingsOpportunities[payload.id - 1],
  riskAreaDetail: (_, payload) => riskAreas[payload.id - 1],
  netSpendDetail: (_, { filterId }) => {
    if (filterId) {
      return {
        ...netSpend,
        spendCategories: netSpend.spendCategories.map(cat => ({
          ...cat,
          amount: `${Math.floor(Math.random() * 1500)}`,
          diff: `${Math.floor(Math.random() * 5) * (Math.random() < 0.5 ? -1 : 1)}`,
        })),
        // spend: netSpend.spend.map(v => ({
        //   ...v,
        //    projSpend: `${Math.floor(Math.random() * 3000)}`,
        //    actualSpend: `${Math.floor(Math.random() * 3000)}`,
        //   delta: Math.floor(((v.projSpend - v.actualSpend) / v.projSpend) * 100),
        //   color: v.projSpend > v.actualSpend ? '#4baaa3' : '#EB707F',
        // })),
      };
    }
    return netSpend;
  },
  teBreakdownDetail: (_, { view, filterId }) => {
    if (filterId) {
      return teBreakdown[view].map(v => ({
        ...v,
        data: v.data.map(expense => ({
          ...expense,
          value: `${Math.floor(Math.random() * 1000)}`,
        })),
      }));
    }
    return teBreakdown[view];
  },
};
