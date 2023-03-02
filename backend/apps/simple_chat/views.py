from typing import Type

from configs.settings import THREAD_CONFIG

from django.contrib.auth import get_user_model
from django.db.models import Count, Q

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    get_object_or_404,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.simple_chat.models import MessageModel, ThreadModel
from apps.simple_chat.serializers import MessageSerializer, ThreadSerializer, ThreadWithMessages
from apps.users.models import UserModel as UserModelTyping

UserModel: Type[UserModelTyping] = get_user_model()


class ThreadListCreateView(ListCreateAPIView):
    queryset = ThreadModel.objects.all()
    user_queryset = UserModel.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = set(self.request.data.get("participants", None))
        if len(data) != THREAD_CONFIG.get("participants_count", 2):
            return Response(
                {"detail": "Can`t create thread. Incorrect number of participants or participant was duplicated"},
                status.HTTP_400_BAD_REQUEST)

        qs = self.get_queryset()
        for pk in data:
            qs = qs.filter(participants=pk)
        qs_exists = qs
        object_exists = qs_exists.exists()
        if object_exists:
            serializer = self.serializer_class(instance=qs.first(), many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        new_thread = self.queryset.create()
        for user in data:
            user_model = get_object_or_404(self.user_queryset, id=user)
            new_thread.participants.add(user_model)
            new_thread.save()
        serializer = self.serializer_class(new_thread, many=False)
        return Response(serializer.data, status.HTTP_200_OK)


class DeleteThreadView(DestroyAPIView):
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        thread_id = self.kwargs.get("thread_id")
        return get_object_or_404(self.queryset, pk=thread_id)


class ThreadListByUserIdView(GenericAPIView):
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadWithMessages
    permission_classes = (AllowAny,)

    def get_queryset(self):
        user = self.kwargs.get("user_id")
        qs = self.queryset.filter(participants__id=user)
        return qs

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        paginated_queryset = self.paginate_queryset(qs)
        serializer = self.serializer_class(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class MessageCreateView(CreateAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        sender_id = self.kwargs.get("sender_id")
        thread_id = self.kwargs.get("thread_id")
        data = self.request.data
        data["sender"] = sender_id
        data["thread"] = thread_id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageInThreadListView(ListAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        thread_id = self.kwargs.get("thread_id")
        qs = self.queryset.filter(thread_id=thread_id)
        return qs


class MessagesIsRead(ListAPIView):
    queryset = MessageModel.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        data = request.data.get("messages_ids", [])
        qs = self.queryset.filter(id__in=data).values("is_read")
        return Response(qs, status=status.HTTP_200_OK)


class CountUserUnreadMessages(ListAPIView):
    queryset = MessageModel.objects.all()

    def list(self, request, *args, **kwargs):
        user_id = kwargs.get("user_id", 0)
        qs = self.queryset.filter(Q(sender_id=user_id) & Q(is_read=False)).aggregate(unread_messages_count=Count("id"))
        return Response(qs, status=status.HTTP_200_OK)
