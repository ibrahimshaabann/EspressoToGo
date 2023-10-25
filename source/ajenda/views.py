from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

from users.models import Person
from .models import Ajenda
from .serializers import AjendaSerializer
from financials.permissions import IsAdminOrEmployee

class AjendaViewSet(ModelViewSet):
    queryset = Ajenda.objects.all()
    serializer_class = AjendaSerializer
    permission_classes = [IsAdminOrEmployee,]
    authentication_classes = [JWTAuthentication,]
    
    def create(self, request, *args, **kwargs):
        user_created_the_ajenda = get_object_or_404(Person, pk=request.user.id)
        request.data["created_by"] = user_created_the_ajenda.id               
        return super().create(request, *args, **kwargs)

