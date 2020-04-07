import graphene
from graphene_django import DjangoObjectType

from .models import historicaldata


class historicaldatatype(DjangoObjectType):
    class Meta:
        model = historicaldata


class Query(graphene.ObjectType):
    data = graphene.List(historicaldatatype)

    def resolve_data(self, info, **kwargs):
        return historicaldata.objects.all()


class CreateData(graphene.Mutation):
    name = graphene.String()
    symbol = graphene.String()
    openingprice = graphene.String()
    closingprice = graphene.String()
    volume = graphene.String()

    #2
    class Arguments:
        name = graphene.String()
        symbol = graphene.String()
        openingprice = graphene.String()
        closingprice = graphene.String()
        volume = graphene.String()

    #3
    def mutate(self, info, name, symbol, openingprice, closingprice, volume):
        historical_data = historicaldata(name = name, symbol = symbol,
        openingprice = openingprice,closingprice = closingprice,volume = volume)
        historical_data.save()



        return CreateData(
            name = historical_data.name,
            symbol = historical_data.symbol,
            openingprice = historical_data.openingprice,
            closingprice = historical_data.closingprice,
            volume = historical_data.volume,
        )


#4
class Mutation(graphene.ObjectType):
    create_data = CreateData.Field()