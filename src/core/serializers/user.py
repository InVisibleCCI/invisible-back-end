from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from common.serializers.entity import EntitySerializer
from core.models import User


class UserRetrieveSerializer(EntitySerializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date_joined = serializers.DateTimeField()

    class Meta:
        model = User
        fields = EntitySerializer.Meta.fields + (
            'email',
            'first_name',
            'last_name',
            'date_joined',
        )


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    date_joined = serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'date_joined'
        )

class EditUserSerializer(WritableNestedModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
        )
