from rest_framework import serializers
from functionbaseviewapp.models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'  #or ['field1', 'field2'] DB fields