const { generateTypeList, generateMutationType } = require('../helper')

exports.divisionDefs = `
${generateTypeList(
  'ClientDivision',
  `{
      id: Int!,
      clientId: Int!,
      divisionName: String!,
      divisionNameFull: String,
      divisionTag: String,
      gcn: String,
      isActive: Boolean!,
      description: String
  }`,
)}

${generateMutationType('UpdateDivisionResponse')}
${generateMutationType('CreateDivisionResponse')}
`

exports.divisionQuery = `
getDivisions(sessionToken: String!, clientId: Int!): ClientDivision
`

exports.divisionMutation = `
updateDivision(
  sessionToken: String!,
  clientDivisionId: Int!,
  divisionName: String!,
  divisionNameFull: String,
  isActive: Boolean!,
  divisionTag: String,
  gcn: String,
  description: String
): UpdateDivisionResponse
createDivision(
  sessionToken: String!,
  clientId: Int!,
  divisionName: String!,
  divisionNameFull: String,
  isActive: Boolean,
  divisionTag: String,
  gcn: String,
  description: String
): CreateDivisionResponse
`