const AWS = require('aws-sdk');
const lambda = new AWS.Lambda();
const { ApolloError } = require('apollo-server-lambda');

exports.lambdaInvoke = async (functionName, payload, dataParam, title) => {
  const params = {
    FunctionName: functionName,
    InvocationType: 'RequestResponse',
    Payload: JSON.stringify(payload),
  };
  const response = await lambda.invoke(params).promise();
  const responseBody = JSON.parse(response.Payload);
  responseBody.body = JSON.parse(responseBody.body);
  if (responseBody.statusCode !== 200) {
    return new ApolloError(responseBody.body.apimessage, 400);
  }
  if (dataParam) {
    responseBody.body.apidataset = responseBody.body.apidataset[dataParam];
    if (title) {
      responseBody.body.apidataset = responseBody.body.apidataset[title];
    }
  }
  return responseBody.body.apidataset;
};
