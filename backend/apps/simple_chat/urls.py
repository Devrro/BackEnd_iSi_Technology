from django.urls import path

from apps.simple_chat.views import (
    CountUserUnreadMessages,
    DeleteThreadView,
    MessageCreateView,
    MessageInThreadListView,
    MessagesIsRead,
    ThreadListByUserIdView,
    ThreadListCreateView,
)

urlpatterns = [
    path("", ThreadListCreateView.as_view(), name="list_threads_view"),
    path("/create_thread", ThreadListCreateView.as_view(), name="create_thread_view"),
    path("/delete_thread/<int:thread_id>", DeleteThreadView.as_view(), name="create_thread_view"),
    path("/list_thread_by_user_id/<int:user_id>", ThreadListByUserIdView.as_view(), name="list_threads_by_user"),
    path("/create_message_in_thread/<int:thread_id>/<int:sender_id>", MessageCreateView.as_view(),
         name="create_message_view"),
    path("/get_messages_in_thread/<int:thread_id>", MessageInThreadListView.as_view(), name="get_messages_in_thread"),
    path("/is_messages_read", MessagesIsRead.as_view(), name="is_messages_read"),
    path("/user_unread_messages_count/<int:user_id>",
         CountUserUnreadMessages.as_view(),
         name="user_unread_messages_count")
]
