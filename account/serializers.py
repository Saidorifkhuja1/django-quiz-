from rest_framework import serializers
from .models import *

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'fullname', 'phonenumber']

    def validate_phonenumber(self, value):
        # Check if the phone number already exists
        if Teacher.objects.filter(phonenumber=value).exists():
            raise serializers.ValidationError("Phone number already exists. Please choose another.")
        return value

    def update(self, instance, validated_data):
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.phonenumber = validated_data.get('phonenumber', instance.phonenumber)
        instance.save()
        return instance

class AccountManagerSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=100)
    phonenumber = serializers.CharField(max_length=21)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        fullname = validated_data['fullname']
        phonenumber = validated_data['phonenumber']
        password = validated_data['password']

        user = AccountManager.objects.create_user(
            fullname=fullname,
            phonenumber=phonenumber,
            password=password
        )
        return user
