const { ApolloServer, gql } = require('apollo-server-lambda');

exports.typeDefs = gql`
  type Action {
    header: String
    secondaryHeader: String
    icon: String
    alert: Boolean
  }

  type Info {
    title: String
    icon: String
    button: String
  }

  type List {
    title: String
    icon: String
    domo: Boolean
    link: String
  }

  type View {
    title: String
    icon: String
    list: [List]
  }

  type Query {
    scott: String
    john: String
    shayan: String
    hanseul: String
    activeAlerts: [Action]
    upcomingActions: [Action]
    infoList: [Info]
    viewList: [View]
  }
`;
