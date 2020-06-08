from rest_framework import serializers
from classbaseviewapp.models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'name', 'score'] #or ['field1', 'field2'] DB fields