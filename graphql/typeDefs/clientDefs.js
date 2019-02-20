const { generateTypeList } = require('../helper')

exports.clientDefs = `
${generateTypeList(
  'Client',
  `{
    id: Int,
    clientName: String,
    clientNameFull: String,
    clientTag: String,
    isActive: Boolean,
    industry: String,
    defaultCurrencyCode: String,
    defaultDistanceUnits: String,
    description: String
}`,
)}
`

exports.clientQuery = `
getClients(sessionToken: String!): Client
`
