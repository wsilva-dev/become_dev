from django.shortcuts import render

# Create your views here.
from .models import Message

def message_list(request):
    messages = Message.objects.order_by("-created_at")
    return render(
        request,
        "board/message_list.html",
        {"messages": messages},
    )
