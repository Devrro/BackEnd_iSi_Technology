from typing import Type

from configs.settings import THREAD_CONFIG

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.validators import ValidationError

from apps.simple_chat.models import MessageModel, ThreadModel
from apps.users.serializers import UserSerializer

participants_count = THREAD_CONFIG.get("participants_count", 2)


class ThreadSerializer(ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = ThreadModel
        fields = (
            "id",
            "participants",
            "created",
            "updated",
        )
        read_only_fields = ("id", "created", "updated")

    def validate_participants(self, value):
        # print(self.initial_data)
        if len(value) > participants_count:
            raise ValidationError({"detail": "Too many participants"})


class MessageSerializer(ModelSerializer):
    class Meta:
        model = MessageModel
        fields = (
            "sender",
            "thread",
            "text",
            "created",
            "is_read",
        )
        read_only_fields = (
            "created",
            "is_read",
        )


class ThreadWithMessages(ModelSerializer):
    message = SerializerMethodField(read_only=True)
    thread = SerializerMethodField(source="id", read_only=True)

    class Meta:
        model = ThreadModel
        fields = (
            "message",
            "thread",
        )

    def get_message(self, obj: ThreadModel):
        message_exists = MessageModel.objects.filter(thread_id=obj.id).exists()
        if message_exists:
            message_obj = MessageModel.objects.filter(thread_id=obj.id).order_by("-created").first()
            serializer = MessageSerializer(message_obj, many=False)
            return serializer.data
        else:
            return {}

    def get_thread(self, obj:ThreadModel):
        serializer = ThreadSerializer(obj)
        return serializer.data
