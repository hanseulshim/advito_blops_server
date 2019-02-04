exports.generateResponse = data => ({
  statusCode: 200,
  body: {
    success: true,
    apicode: 'OK',
    apimessage: 'User successfully logged in.',
    apidataset: data,
  },
});

exports.generateType = (type, data) => `
type ${type}Data ${data}

type ${type}Body {
  success: Boolean,
  apicode: String,
  apimessage: String,
  apidataset: ${type}Data
}

type ${type} {
  statusCode: Int,
  body: ${type}Body
}`;

exports.generateTypeList = (type, data) => `
type ${type}Data ${data}

type ${type}Body {
  success: Boolean,
  apicode: String,
  apimessage: String,
  apidataset: [${type}Data]
}

type ${type} {
  statusCode: Int,
  body: ${type}Body
}`;

exports.generateQuery = (query, data) => `
${query}(clientId: Int!, sessionToken: String!): ${data}
`;
