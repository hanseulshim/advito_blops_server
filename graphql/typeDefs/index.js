const { gql } = require('apollo-server-lambda');
const { consoleDefs, consoleQuery } = require('./consoleDefs');
const { storyDefs, storyQuery } = require('./storyDefs');
const { loginDefs, loginQuery } = require('./loginDefs');
const { userDefs, userQuery } = require('./userDefs');

exports.typeDefs = gql`
  ${consoleDefs}
  ${storyDefs}
  ${loginDefs}
  ${userDefs}
  type Query {
    ${consoleQuery}
    ${storyQuery}
    ${loginQuery}
    ${userQuery}
  }
`;
