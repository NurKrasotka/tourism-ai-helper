from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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
