exports.portalDefs = `
type UpcomingAction {
  header: String
  secondaryHeader: String
  icon: String
  alert: Boolean
}
type ActiveAlert {
  header: String
  secondaryHeader: String
  icon: String
  alert: Boolean
}
type Product {
  title: String
  icon: String
  optionList: [ProductOption]
  disabled: Boolean
}
type ProductOption {
  title: String
  icon: String
  domo: Boolean
  link: String
}
type ProductEvent {
  title: String
  description: String
  icon: String
  disabled: Boolean
  button: String
}
`;

exports.portalQueries = `
  upcomingActionList: [UpcomingAction] @auth
  activeAlertList: [ActiveAlert] @auth
  productList: [Product] @auth
  productEventList: [ProductEvent] @auth
`;
