import graphene

def dummy_login(username, password):
    return True

class Query(graphene.ObjectType):
    login = graphene.Boolean(username=graphene.String(), password=graphene.String())

    def resolve_login(self, info, username, password):
        return dummy_login(username, password)

schema = graphene.Schema(query=Query)



