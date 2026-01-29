from django.http import HttpResponse
from django.shortcuts import redirect, render

from notes.models import Note

# Create your views here.
def index(request):
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Note.objects.create(content=content)
        return redirect("index")
    
    notes = Note.objects.all()
    return render(request, "notes/index.html", {
        "notes": notes
    })

