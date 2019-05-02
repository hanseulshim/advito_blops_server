exports.clientDefs = `
type Client {
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
  description: String,
  divisions: [ClientDivision!]
}
`;

exports.clientQuery = `
clientList: [Client] @auth
`;
exports.clientMutation = `
updateClient(
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
): String @auth
createClient(
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
): String @auth
`;
