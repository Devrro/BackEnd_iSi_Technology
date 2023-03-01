from rest_framework.serializers import ModelSerializer


class ThreadSerializer:
    class Meta:
        fields = "__all__"


class MessageSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
