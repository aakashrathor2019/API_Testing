from rest_framework import serializers
from django_rest.models import Student,Book,Category


class StudentSerializer(serializers.ModelSerializer):

  class Meta:
     model=Student
     fields='__all__'


  def validate_st_name(self,value):
     
     if any(char.isdigit()  for char in value):
        raise serializers.ValidationError('Name must contaion characters only')
     
     return value
  

class CategorySerializer(serializers.ModelSerializer):
   
   class Meta:
      model=Category
      fields='__all__'


class BookSerializer(serializers.ModelSerializer):
   category=CategorySerializer()
   class Meta:
      model=Book
      fields='__all__'