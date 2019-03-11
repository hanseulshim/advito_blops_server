exports.applicationDefs = `
type Application {
  id: Int,
  applicationName: String,
  applicationFull: String,
  applicationTag: String,
  isActive: Boolean,
  description: String,
  features: [ApplicationFeature]
}
type ApplicationFeature {
  id: Int,
  featureName: String,
  featureTag: String,
  isActive: Boolean,
  description: String
}
`;

exports.applicationQuery = `
applicationList(clientId: Int): [Application] @auth
`;
exports.applicationMutation = `
setFeatures(
  clientId: Int!,
  featureIds: [Int]
): [Int] @auth
`;
