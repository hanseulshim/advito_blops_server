const { consoleResolvers } = require('./consoleResolvers')
const { storyResolvers } = require('./storyResolvers')
const { userResolvers, userResolversMutation } = require('./userResolvers')
const {
  clientResolvers,
  clientResolversMutation,
} = require('./clientResolvers')
const {
  divisionResolvers,
  divisionResolversMutation,
} = require('./divisionResolvers')
const {
  savingsOpportunityDetailResolvers,
} = require('./savingsOpportunityDetailResolvers')
const { riskAreaDetailResolvers } = require('./riskAreaDetailResolvers')
const { generateResponse, lambdaInvoke } = require('../helper')

exports.resolvers = {
  Query: {
    ...consoleResolvers,
    ...storyResolvers,
    ...userResolvers,
    ...clientResolvers,
    ...divisionResolvers,
    ...savingsOpportunityDetailResolvers,
    ...riskAreaDetailResolvers,
    login: (_, payload) => {
      return lambdaInvoke('python-lambdas-dev-user_login', {
        username: payload.username,
        pwd: payload.pwd,
      })
    },
    logout: (_, payload) => {
      return lambdaInvoke('python-lambdas-dev-user_logout', {
        ...payload,
      })
    },
  },
  Mutation: {
    ...userResolversMutation,
    ...clientResolversMutation,
    ...divisionResolversMutation,
  },
}
