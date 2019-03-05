exports.portal = {
  name: 'Portal Queries',
  endpoint: 'http://localhost:8080/graphql',
  headers: { sessiontoken: 'advitoValidToken' },
  query: `
  {
    upcomingActionList {
      header
      secondaryHeader
      icon
      alert
    }
    activeAlertList {
      header
      secondaryHeader
      icon
      alert
    }
    productList {
      title
      icon
      optionList {
        title
        icon
        domo
        link
      }
      disabled
    }
    productEventList {
      title
      description
      icon
      disabled
      button
    }
  }`,
};
