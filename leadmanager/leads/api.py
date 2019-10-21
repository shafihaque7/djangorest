from .models import Lead
from .models import Salary, Paradigm, Language, Programmer
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer,SalarySerializer, ParadigmSerializer, LanguageSerializer, ProgrammerSerializer

# Lead Viewset

class LeadViewSet(viewsets.ModelViewSet):
   queryset = Lead.objects.all()
   permission_classes = [
      permissions.AllowAny
   ]
   serializer_class = LeadSerializer
   
class SalaryViewSet(viewsets.ModelViewSet):
   queryset = Salary.objects.all()
   permission_classes = [
      permissions.AllowAny
   ]
   serializer_class = SalarySerializer

class ParadigmViewset(viewsets.ModelViewSet):
   queryset = Paradigm.objects.all()
   permission_classes = [
      permissions.AllowAny
   ]
   serializer_class = ParadigmSerializer

class LanguageViewset(viewsets.ModelViewSet):
   queryset = Language.objects.all()
   permission_classes = [
      permissions.AllowAny
   ]
   serializer_class = LanguageSerializer

class ProgrammerViewset(viewsets.ModelViewSet):
   queryset = Programmer.objects.all()
   permission_classes = [
      permissions.AllowAny
   ]
   serializer_class = ProgrammerSerializer


   