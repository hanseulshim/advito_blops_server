const { gql } = require('apollo-server-lambda');
const { storyDefs, storyQuery } = require('./storyDefs');
const { clientDefs, clientQuery, clientMutation } = require('./clientDefs');
const { userDefs, userQuery, userMutation } = require('./userDefs');
const {
  divisionDefs,
  divisionQuery,
  divisionMutation,
} = require('./divisionDefs');

const { loginDefs, loginQuery } = require('./login');
const { portalDefs, portalQueries } = require('./portal');
const { travelManagerDefs, travelManagerQueries } = require('./travelManager');
const { executiveDefs, executiveQueries } = require('./executive');

exports.typeDefs = gql`
directive @auth on FIELD_DEFINITION
  ${loginDefs}
  ${portalDefs}
  ${travelManagerDefs}
  ${executiveDefs}

  ${storyDefs}
  ${clientDefs}
  ${userDefs}
  ${divisionDefs}
  type Query {
    ${loginQuery}
    ${portalQueries}
    ${travelManagerQueries}
    ${executiveQueries}


    ${storyQuery}
    ${userQuery}
    ${clientQuery}
    ${divisionQuery}
  }
  type Mutation {
    ${userMutation}
    ${clientMutation}
    ${divisionMutation}
  }
`;
