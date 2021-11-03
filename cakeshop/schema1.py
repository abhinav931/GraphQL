import graphene
from graphene_django import DjangoObjectType
from graphene import relay, ObjectType
from cakeshop.models import Cake, Flavor
from graphene_django.filter import DjangoFilterConnectionField


class FlavorNode(DjangoObjectType):
    class Meta:
        model = Flavor
        filter_fields = ['name', 'id']
        interfaces = (relay.Node, )


class CakeNode(DjangoObjectType):
    class Meta:
        model = Cake
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'flavor': ['exact'],
            'flavor__name': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    flavor = relay.Node.Field(FlavorNode)
    all_flavors = DjangoFilterConnectionField(FlavorNode)

    cake = relay.Node.Field(CakeNode)
    all_cakes = DjangoFilterConnectionField(CakeNode
                                            )


schema1 = graphene.Schema(query=Query)
