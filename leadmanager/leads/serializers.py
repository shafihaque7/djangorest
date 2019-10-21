from rest_framework import serializers
from leads.models import Lead,Salary, Language, Paradigm, Programmer


class LeadSerializer(serializers.ModelSerializer):
   class Meta:
      model = Lead
      fields = '__all__'
      
class SalarySerializer(serializers.ModelSerializer):
   class Meta:
      model = Salary
      fields = '__all__'


class ParadigmSerializer(serializers.ModelSerializer):
   class Meta:
      model = Paradigm
      fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
   class Meta:
      model = Language
      fields = '__all__'

class ProgrammerSerializer(serializers.ModelSerializer):
   class Meta:
      model = Programmer
      fields = '__all__'