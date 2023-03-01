from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework.serializers import ModelSerializer

from apps.users.models import ProfileModel

UserModel = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id',
            'email',
            'password',
            'created_at',
            'updated_at',
            'is_staff',
            'is_active',
            'is_superuser',
            'profile',
        )
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
            'is_staff',
            'is_active',
            'is_superuser',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    @atomic
    def create(self, validated_data):
        profile = validated_data.pop("profile")
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(user=user, **profile)
        return user
