const {
  activeAlertList,
  upcomingActionList,
  productList,
  productEventList,
} = require('../../data/portal');

exports.portalQueries = {
  upcomingActionList: () => upcomingActionList,
  activeAlertList: () => activeAlertList,
  productList: () => productList,
  productEventList: () => productEventList,
};
