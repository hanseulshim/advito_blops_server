const { gql } = require('apollo-server-lambda');
const { consoleDefs, consoleQuery } = require('./consoleDefs');
const { storyDefs, storyQuery } = require('./storyDefs');
const { loginDefs, loginQuery } = require('./loginDefs');

exports.typeDefs = gql`
  ${consoleDefs}
  ${storyDefs}
  ${loginDefs}
  type Query {
    ${consoleQuery}
    ${storyQuery}
    ${loginQuery}
  }
`;
