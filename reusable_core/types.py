import graphene
from reusable_core.connections import TotalItemsConnection


class UserRemoteType(graphene.ObjectType):
    id = graphene.ID()
    email = graphene.String()
    cpf = graphene.String()
    phone = graphene.String()
    username = graphene.String()
    birthDate = graphene.String()
    cep = graphene.String()
    street = graphene.String()
    number = graphene.Int()
    neighborhood = graphene.String()
    complement = graphene.String()
    cityName = graphene.String()
    cityStateName = graphene.String()
    userType = graphene.String()

    class Meta:
        fields = ['id', 'email', 'cpf', 'phone', 'username', 'birthDate', 'cep', 'street',
                  'number', 'neighborhood', 'complement', 'cityName', 'cityStateName', 'userType', ]
        connection_class = TotalItemsConnection
        use_connection = True
