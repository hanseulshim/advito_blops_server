const {
  SchemaDirectiveVisitor,
  AuthenticationError,
} = require('apollo-server-lambda');

class RequireAuthDirective extends SchemaDirectiveVisitor {
  visitFieldDefinition(field) {
    const { resolve = defaultFieldResolver } = field;
    field.resolve = async (...args) => {
      const [, , context] = args;
      if (context.user) {
        const result = await resolve.apply(this, args);
        return result;
      } else {
        throw new AuthenticationError(
          'You must be signed in to view this resource.',
        );
      }
    };
  }
}

module.exports = RequireAuthDirective;
