exports.quarterFilterDefs = `
type QuarterFilter {
  id: Int,
  value: String
}
`;

exports.quarterFilterQueries = `
  quarterFilterList: [QuarterFilter] @auth
`;
