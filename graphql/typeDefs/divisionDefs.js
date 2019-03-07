exports.divisionDefs = `
type ClientDivision {
  id: Int!,
  clientId: Int!,
  divisionName: String!,
  divisionNameFull: String,
  divisionTag: String,
  gcn: String,
  isActive: Boolean!,
  description: String
}
`;

exports.divisionQuery = `
divisionList(clientId: Int!): [ClientDivision] @auth
`;

exports.divisionMutation = `
updateDivision(
  id: Int!,
  divisionName: String!,
  divisionNameFull: String,
  isActive: Boolean!,
  divisionTag: String,
  gcn: String,
  description: String
): ClientDivision @auth
createDivision(
  clientId: Int!,
  divisionName: String!,
  divisionNameFull: String,
  isActive: Boolean,
  divisionTag: String,
  gcn: String,
  description: String
): String @auth
`;
