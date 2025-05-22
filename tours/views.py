from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.shortcuts import render, get_object_or_404
from .models import Category, Tour

# 🔧 Импорт функции из ai_helper.py в том же приложении (tours)
from .ai_helper import ask_chatgpt

def chat_page(request):
    return render(request, "chat.html")

@csrf_exempt
def chat_with_ai(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')
        answer = ask_chatgpt(user_message)
        return JsonResponse({'response': answer})
    
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)



def home_page(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    tours = Tour.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'tours': tours})

def book_tour(request, tour_id):
    return HttpResponse(f"Забронирован тур с ID {tour_id}")
