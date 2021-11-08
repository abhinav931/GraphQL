from graphene import relay
import graphene
from graphene_django import DjangoObjectType

from cakeshop.schema import CakeType
from .models import Cake


class QuestionType(DjangoObjectType):
    class Meta:
        model = Cake
        interfaces = (relay.Node,)  # make sure you add this
        fields = "__all__"


class CakeConnection(relay.Connection):
    class Meta:
        node = CakeType


class Query(graphene.ObjectType):
    cakes = relay.ConnectionField(CakeConnection)

    def resolve_cakes(root, info, **kwargs):
        return Cake.objects.all()


schema2 = graphene.Schema(query=Query)
