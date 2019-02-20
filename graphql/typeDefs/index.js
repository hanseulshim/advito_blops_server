const { gql } = require('apollo-server-lambda');
const { consoleDefs, consoleQuery } = require('./consoleDefs');
const { storyDefs, storyQuery } = require('./storyDefs');
const { loginDefs, loginQuery } = require('./loginDefs');
const { clientDefs, clientQuery } = require('./clientDefs');
const { userDefs, userQuery, userMutation } = require('./userDefs');

exports.typeDefs = gql`
  ${consoleDefs}
  ${storyDefs}
  ${loginDefs}
  ${clientDefs}
  ${userDefs}
  type Query {
    ${consoleQuery}
    ${storyQuery}
    ${loginQuery}
    ${userQuery}
    ${clientQuery}
  }
  type Mutation {
    ${userMutation}
  }
`;
