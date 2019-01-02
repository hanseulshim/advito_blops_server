const { gql } = require('apollo-server-lambda');
const { consoleDefs, consoleQuery } = require('./consoleDefs');
const { storyDefs, storyQuery } = require('./storyDefs');

exports.typeDefs = gql`
  ${consoleDefs}
  ${storyDefs}
  type Query {
    ${consoleQuery}
    ${storyQuery}
  }
`;
