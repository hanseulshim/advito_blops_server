const { dashboardQueries } = require('./dashboard');
// const { categoryQueries } = require('./category');

exports.executiveQueries = {
  ...dashboardQueries,
  // ...categoryQueries,
};
