import graphene
import graphql_jwt

import src.links.schema
import src.accounts.schema


class Query(src.links.schema.Query,
            src.accounts.schema.Query,
            graphene.ObjectType):
    pass


class Mutation(src.links.schema.Mutation,
               src.accounts.schema.Mutation,
               graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
