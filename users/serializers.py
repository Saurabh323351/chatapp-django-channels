from rest_framework import serializers
# from .models import Employee, Department
from django.contrib.auth.models import User
#
#
# class EmployeeSerializer(serializers.Serializer):
#     eno = serializers.IntegerField()
#     ename = serializers.CharField(max_length=100)
#     esal = serializers.FloatField()
#     eaddr = serializers.CharField(max_length=300)
#     user = serializers.CharField(max_length=100, required=False)
#
#     def create(self, validated_data):
#         print('-------->', validated_data, '----------->')
#
#         """
#         First Approach to save data in db
#
#         obj=Employee(**validated_data)
#         obj.save()
#         """
#
#         """
#         Second Approach to svae data to database
#         """
#
#         obj = Employee.objects.create(**validated_data)
#
#         print(obj, '------------>create obj')
#         return obj
#
#     def update(self, instance, validated_data):
#         print('-------->', validated_data, '----------->')
#         instance.eno = validated_data.get('eno', instance.eno)
#         instance.ename = validated_data.get('ename', instance.ename)
#         instance.esal = validated_data.get('esal', instance.esal)
#         instance.eaddr = validated_data.get('eaddr', instance.eaddr)
#         instance.user = validated_data.get('user', instance.user)
#
#         instance.save()
#
#         return instance
#
#
# class DepartmentModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         fields = ['id', 'department_name']


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']