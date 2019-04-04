exports.dashboard = {
  name: 'Travel Manager Dashboard Queries',
  endpoint: 'http://localhost:8080/graphql',
  headers: { sessiontoken: 'advitoValidToken' },
  query: `
  {
    noFilterprogramPerformanceListTravel: programPerformanceListTravel {
      id
      title
      value
      unit
    }
    filterprogramPerformanceListTravel: programPerformanceListTravel(filterId: 1) {
      id
      title
      value
      unit
    }
    netSpendAnalysisListTravel {
      date
      value
    }
    personaList {
      title
      value
      programShare
    }
    savingsOpportunityFeedTravel(limit: 3, cursor: 0) {
      prevCursor
      cursor
      totalSavingsOpportunities
      hasNext
      savingsOpportunityList {
        id
        title
        value
        secondaryValue
        unit
        secondaryUnit
      }
    }
    riskAreaFeedTravel(limit: 3, cursor: 0) {
      prevCursor
      cursor
      totalRiskAreas
      hasNext
      riskAreaList {
        id
        title
        value
        secondaryValue
        unit
        secondaryUnit
      }
    }
    noChangeSince
  }`,
};
