const AWS = require('aws-sdk');
const lambda = new AWS.Lambda();

exports.generateResponse = data => ({
  statusCode: 200,
  body: {
    success: true,
    apicode: 'OK',
    apimessage: 'This is a fake response!',
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

exports.lambdaInvoke = async (functionName, payload, dataParam) => {
  const params = {
    FunctionName: functionName,
    InvocationType: 'RequestResponse',
    Payload: JSON.stringify(payload),
  };
  const response = await lambda.invoke(params).promise();
  const responseBody = JSON.parse(response.Payload);
  responseBody.body = JSON.parse(responseBody.body);
  if (dataParam) {
    responseBody.body.apidataset = responseBody.body.apidataset[dataParam];
  }
  return responseBody;
};

exports.lambdaFakeInvoke = async (payload, data) => {
  const params = {
    FunctionName: 'python-lambdas-dev-udf_story_hotel_3',
    InvocationType: 'RequestResponse',
    Payload: JSON.stringify(payload),
  };
  const response = await lambda.invoke(params).promise();
  const responseBody = JSON.parse(response.Payload);
  responseBody.body = JSON.parse(responseBody.body);
  if (responseBody.statusCode === 200) {
    return exports.generateResponse(data);
  } else {
    return responseBody;
  }
};
