const { generateTypeList, generateMutationType } = require('../helper')

exports.clientDefs = `
${generateTypeList(
  'Client',
  `{
    id: Int,
    clientName: String,
    clientNameFull: String,
    clientTag: String,
    gcn: String,
    lanyonClientCode: String,
    isActive: Boolean,
    industry: String,
    defaultCurrencyCode: String,
    defaultDistanceUnits: String,
    description: String
}`,
)}

${generateMutationType('UpdateClientResponse')}
${generateMutationType('CreateClientResponse')}
`

exports.clientQuery = `
getClients(sessionToken: String!): Client
`
exports.clientMutation = `
updateClient(
  sessionToken: String!,
  clientId: Int!,
  clientName: String!,
  clientNameFull: String,
  clientTag: String,
  gcn: String,
  lanyonClientCode: String,
  isActive: Boolean!,
  logoPath: String,
  industry: String,
  defaultCurrencyCode: String,
  defaultDistanceUnits: String,
  description: String
): UpdateClientResponse
createClient(
  sessionToken: String!,
  clientName: String!,
  clientNameFull: String,
  clientTag: String,
  gcn: String,
  lanyonClientCode: String,
  isActive: Boolean!,
  logoPath: String,
  industry: String,
  defaultCurrencyCode: String,
  defaultDistanceUnits: String,
  description: String
): CreateClientResponse
`