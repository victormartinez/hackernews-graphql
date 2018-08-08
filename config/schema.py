import graphene
import src.links.schema


class Query(src.links.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
