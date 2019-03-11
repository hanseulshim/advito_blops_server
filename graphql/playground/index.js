const { login } = require('./login');
const { portal } = require('./portal');
const { travelManagerTabs } = require('./travelManager');
const { executiveTabs } = require('./executive');
const { story } = require('./story');
const { userQueries, userMutations } = require('./user');
const { clientQueries, clientMutations } = require('./client');
const { divisionQueries, divisionMutations } = require('./division');
const { applicationQueries, applicationMutations } = require('./application');
exports.playground = {
  tabs: [
    login,
    portal,
    ...travelManagerTabs,
    ...executiveTabs,
    story,
    userQueries,
    userMutations,
    clientQueries,
    clientMutations,
    divisionQueries,
    divisionMutations,
    applicationQueries,
    applicationMutations
  ],
};
