from django.urls import path
from .views import book_tour, chat_page, chat_with_ai, home_page, category_detail

urlpatterns = [
    path('', home_page, name='home'),
    path('chat/', chat_with_ai, name='chat'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('book/<int:tour_id>/', book_tour, name='book_tour'),
]
