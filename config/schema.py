import graphene
import src.links.schema
import src.accounts.schema


class Query(src.links.schema.Query,
            src.accounts.schema.Query,
            graphene.ObjectType):
    pass


class Mutation(src.links.schema.Mutation,
               src.accounts.schema.Mutation,
               graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
