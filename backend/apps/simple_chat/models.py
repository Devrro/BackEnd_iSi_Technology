from __future__ import annotations

from django.contrib.auth import get_user_model
from django.db import models

from apps.users.models import UserModel as UserModelTyping

UserModel: UserModelTyping = get_user_model()


class ThreadModel(models.Model):
    participants = models.ManyToManyField(
        UserModel, related_name="thread_participants")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "thread"

    def __str__(self):
        return f"ThreadID - {self.id}"


class MessageModel(models.Model):
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="sender")
    thread = models.ForeignKey(ThreadModel, on_delete=models.CASCADE, related_name="thread")
    text = models.TextField(
        blank=False
    )
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        db_table = "message"

    def __str__(self):
        return f"UserID - {self.sender} | is_read - {self.is_read}"
