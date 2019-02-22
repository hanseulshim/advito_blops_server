const { gql } = require('apollo-server-lambda');
const { consoleDefs, consoleQuery } = require('./consoleDefs');
const { storyDefs, storyQuery } = require('./storyDefs');
const { loginDefs, loginQuery } = require('./loginDefs');
const { clientDefs, clientQuery, clientMutation } = require('./clientDefs');
const { userDefs, userQuery, userMutation } = require('./userDefs');
const { divisionDefs, divisionQuery, divisionMutation } = require('./divisionDefs');

exports.typeDefs = gql`
  ${consoleDefs}
  ${storyDefs}
  ${loginDefs}
  ${clientDefs}
  ${userDefs}
  ${divisionDefs}
  type Query {
    ${consoleQuery}
    ${storyQuery}
    ${loginQuery}
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
