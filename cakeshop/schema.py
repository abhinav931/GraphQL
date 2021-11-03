import graphene
from graphene_django import DjangoObjectType

from cakeshop.models import Cake, Flavor


class CakeType(DjangoObjectType):

    class Meta:
        model = Cake
        fields = "__all__"


class FlavorType(DjangoObjectType):

    class Meta:
        model = Flavor
        fields = "__all__"


class Query(graphene.ObjectType):
    all_cakes = graphene.List(CakeType)
    flavor_by_name = graphene.Field(
        FlavorType, name=graphene.String(required=False))

    def resolve_all_cakes(root, info):
        return Cake.objects.select_related("flavor").all()

    def resolve_flavor_by_name(root, info, name):
        if not name:
            return Flavor.objects.all().first()
        return Flavor.objects.get(name=name)


schema = graphene.Schema(query=Query)
