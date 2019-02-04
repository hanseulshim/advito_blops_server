const { generateType, generateTypeList, generateQuery } = require('../helper');

exports.consoleDefs = `
${generateTypeList(
  'Action',
  `{
    header: String
    secondaryHeader: String
    icon: String
    alert: Boolean
  }`
)}

${generateTypeList(
  'Info',
  `{
    title: String
    description: String
    icon: String
    disabled: Boolean
    button: String
  }`
)}

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

${generateType(
  'OpportunityFeed',
  `{
    prevCursor: Int
    cursor: Int
    totalOpportunities: Int
    hasNext: Boolean
    opportunities: [Opportunity]
  }`
)}

${generateTypeList(
  'Performance',
  `{
    title: String
    value: String
    unit: String
  }`
)}

${generateTypeList(
  'Persona',
  `{
    title: String
    value: String
    programShare: Int
    color: String
  }`
)}

type RiskArea {
  title: String
  value: String
}

${generateType(
  'RiskAreaFeed',
  `{
    prevCursor: Int
    cursor: Int
    totalRiskAreas: Int
    hasNext: Boolean
    riskAreas: [RiskArea]
  }`
)}

${generateTypeList(
  'View',
  `{
    title: String
    icon: String
    list: [List]
    disabled: Boolean
  }`
)}

type NoChangeSinceBody {
  success: Boolean,
  apicode: String,
  apimessage: String,
  apidataset: String,
}

type NoChangeSince {
  statusCode: Int,
  body: NoChangeSinceBody
}
`;

exports.consoleQuery = `
${generateQuery('activeAlerts', 'Action')}
${generateQuery('upcomingActions', 'Action')}
${generateQuery('infoData', 'Info')}
${generateQuery('viewData', 'View')}
${generateQuery('programPerformance', 'Performance')}
${generateQuery('noChangeSince', 'NoChangeSince')}
${generateQuery('personaList', 'Persona')}
opportunities(clientId: Int!, sessionToken: String!, limit: Int, cursor: Int): OpportunityFeed
riskAreas(clientId: Int!, sessionToken: String!, limit: Int, cursor: Int): RiskAreaFeed`;
