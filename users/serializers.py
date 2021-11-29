from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
import django.contrib.auth.password_validation as validators
from rest_framework.exceptions import ValidationError

class ModelUserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "roles",
            "password"
        ]
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        try:
            validated_data['password'] = make_password(
                validated_data['password'])
        except Exception:
            pass
        user = get_user_model().objects.create(**validated_data)
        return user
