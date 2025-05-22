from django.urls import path
from .views import chat_page, chat_with_ai

urlpatterns = [
    path('', chat_page, name='chat_page'),
    path('chat/', chat_with_ai, name='chat'),  # ✅ будет доступен как /api/chat/
]