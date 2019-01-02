exports.consoleDefs = `type Action {
  header: String
  secondaryHeader: String
  icon: String
  alert: Boolean
}

type Info {
  title: String
  description: String
  icon: String
  disabled: Boolean
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
  unit: String
}

type OpportunityFeed {
  prevCursor: Int
  cursor: Int
  totalOpportunities: Int
  hasNext: Boolean
  opportunities: [Opportunity]
}

type Performance {
  title: String
  value: String
  unit: String
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

type RiskAreaFeed {
  prevCursor: Int
  cursor: Int
  totalRiskAreas: Int
  hasNext: Boolean
  riskAreas: [RiskArea]
}

type View {
  title: String
  icon: String
  list: [List]
  disabled: Boolean
}

type Login {
  user_id: Int
  displayname: String
  email: String
  session_token: String
}`;

exports.consoleQuery = `activeAlerts: [Action]
upcomingActions: [Action]
infoData: [Info]
viewData: [View]
programPerformance: [Performance]
noChangeSince: String
personaList: [Persona]
opportunities(limit: Int, cursor: Int): OpportunityFeed
riskAreas(limit: Int, cursor: Int): RiskAreaFeed`;
