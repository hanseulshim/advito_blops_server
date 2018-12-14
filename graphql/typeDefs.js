const { gql } = require('apollo-server-lambda');

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

  type Opportunity {
    title: String
    value: String
  }

  type Performance {
    title: String
    value: String
  }

  type Persona {
    title: String
    value: String
    programShare: Int
    color: String
  }

  type RiskArea {
    title: String
    value: String
  }

  type View {
    title: String
    icon: String
    list: [List]
  }

  type Login {
    user_id: Int
    displayname: String
    email: String
    session_token: String
  }

  type Query {
    activeAlerts: [Action]
    upcomingActions: [Action]
    infoList: [Info]
    viewList: [View]
    performanceList: [Performance]
    noChangeSince: String
    personaList: [Persona]
    opportunities: [Opportunity]
    riskAreas: [RiskArea]
    logins(username: String, password: String): Login
  }
`;
