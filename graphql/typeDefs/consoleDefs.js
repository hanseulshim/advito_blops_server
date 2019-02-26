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

type Division {
  title: String,
  value: String,
  secondaryValue: String,
  unit: String,
  secondaryUnit: String,
}

type Opportunity {
  id: Int
  title: String
  value: String
  unit: String
  secondaryValue: String
  secondaryUnit: String
  divisions: [Division]
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
  'ProgramPerformanceTravel',
  `{
    title: String
    value: String
    unit: String
  }`
)}

${generateType(
  'ProgramPerformanceExecutive',
  `{
    value: Float
  }`
)}

${generateTypeList(
  'NetSpendAnalysisTravel',
  `{
    date: String
    value: Float
  }`
)}

${generateTypeList(
  'NetSpendAnalysisExecutive',
  `{
    date: String
    value: Float
  }`
)}

${generateTypeList(
  'Persona',
  `{
    title: String
    value: String
    programShare: Int
  }`
)}

${generateTypeList(
  'Market',
  `{
    title: String
    value: Float
    programShare: Int
  }`
)}

type RiskArea {
  title: String
  value: String
  unit: String
  secondaryValue: String
  secondaryUnit: String
  divisions: [Division]
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
${generateQuery('programPerformanceTravel', 'ProgramPerformanceTravel')}
${generateQuery('programPerformanceExecutive', 'ProgramPerformanceExecutive')}
${generateQuery('netSpendAnalysisTravel', 'NetSpendAnalysisTravel')}
${generateQuery('netSpendAnalysisExecutive', 'NetSpendAnalysisExecutive')}
${generateQuery('noChangeSince', 'NoChangeSince')}
${generateQuery('personaList', 'Persona')}
${generateQuery('marketList', 'Market')}
opportunitiesTravel(clientId: Int!, sessionToken: String!, limit: Int, cursor: Int): OpportunityFeed
opportunitiesExecutive(clientId: Int!, sessionToken: String!, limit: Int, cursor: Int): OpportunityFeed
riskAreasTravel(clientId: Int!, sessionToken: String!, limit: Int, cursor: Int): RiskAreaFeed
riskAreasExecutive(clientId: Int!, sessionToken: String!, limit: Int, cursor: Int): RiskAreaFeed`;
