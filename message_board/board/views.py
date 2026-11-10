from django.shortcuts import render, redirect

# Create your views here.
from .models import Message

def message_list(request):
    messages = Message.objects.order_by("-created_at") # minus sign sorts in reverse order based on the field "created_at"
    total_messages = messages.count()
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

def message_create(request):
    if request.method == "POST":
        author = request.POST.get("author", "").strip()
        content = request.POST.get("content", "").strip()

        if author and content and len(author) <=100:
            Message.objects.create( # create the register in the date base
                author=author,
                content=content,
            )
            return redirect('message_list') 

        return render(
            request, "board/novo_recado.html", {
                "error" : "Preencha os dois campos. O autor deve ter até 100 caracteres.",
                "author" : author,
                "content" : content,
            })
    
    return render(request, "board/novo_recado.html")
