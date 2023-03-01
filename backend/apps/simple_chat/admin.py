from django.contrib import admin
from django.db import models

from apps.simple_chat.models import MessageModel, ThreadModel


class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "thread", "text", "is_read", "created")
    list_filter = ("is_read", "created")
    search_fields = ("sender",)


class MessageInline(admin.TabularInline):
    model = MessageModel
    extra = 0


class ThreadAdmin(admin.ModelAdmin):
    inlines = (MessageInline,)
    list_display = ("id", "created", "updated")
    list_filter = ("id", "created", "updated")


admin.site.register(MessageModel, MessageAdmin)
admin.site.register(ThreadModel, ThreadAdmin)
