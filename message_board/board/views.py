from django.shortcuts import render

# Create your views here.
from .models import Message

def message_list(request):
    messages = Message.objects.order_by("-created_at") # minus sign sorts in reverse order based on the field "created_at"
    total_messages = messages.count
    return render(
        request,
        "board/message_list.html",
        {
            "messages": messages,
            "total_messages" : total_messages,
         },
    )

def about(request):
    return render(request, "board/about.html")
