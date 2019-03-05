const { dashboardQueries } = require('./dashboard');
const { categoryQueries } = require('./category');

exports.travelManagerQueries = {
  ...dashboardQueries,
  ...categoryQueries,
};
