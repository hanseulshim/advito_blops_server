exports.dashboard = {
  name: 'Executive Manager Dashboard Queries',
  endpoint: 'http://localhost:8080/graphql',
  headers: { sessiontoken: 'advitoValidToken' },
  query: `
  {
    programPerformanceExecutive {
      value
    }
    netSpendAnalysisListExecutive {
      date
      value
    }
    marketList {
      title
      value
      programShare
    }
    savingsOpportunityFeedExecutive(limit: 3, cursor: 0) {
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
        divisionList {
          title
          value
          secondaryValue
          unit
          secondaryUnit
        }
      }
    }
    riskAreaFeedExecutive(limit: 3, cursor: 0) {
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
        divisionList {
          title
          value
          secondaryValue
          unit
          secondaryUnit
        }
      }
    }
  }`,
};
