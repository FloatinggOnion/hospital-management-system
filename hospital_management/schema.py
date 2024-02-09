import graphene
from graphene_django import DjangoObjectType
from core.models import Hospital


class HospitalType(DjangoObjectType):
    class Meta:
        model = Hospital
        field = ('id', 'name', 'address', 'phone_number', 'email', 'website', 'capacity')


class Query(graphene.ObjectType):
    all_hospitals = graphene.List(HospitalType)

    def resolve_all_hospitals(self, info, **kwargs):
        return Hospital.objects.all()
    
    hospital = graphene.Field(HospitalType, id=graphene.Int())

    def resolve_hospital(self, info, id):
        return Hospital.objects.get(pk=id)
    

class HospitalMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        address = graphene.String()
        phone_number = graphene.String()
        email = graphene.String()
        website = graphene.String()
        capacity = graphene.Int()
    
    hospital = graphene.Field(HospitalType)

    @classmethod
    def mutate(cls, root, info, name, address, phone_number, email, website, capacity):
        ######## Create ########
        hospital = Hospital(name=name, address=address, phone_number=phone_number, email=email, website=website, capacity=capacity)
        hospital.save()

        return HospitalMutation(hospital=hospital)
    

class Mutation(graphene.ObjectType):
    create_hospital = HospitalMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)