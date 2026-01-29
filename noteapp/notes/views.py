from django.http import HttpResponse
from django.shortcuts import redirect, render
from django import forms

from notes.models import Note

# Create your views here.
class NoteForm(forms.Form):
    note = forms.CharField(max_length=100)
    status = forms.BooleanField(required=False)

def index(request):
    if request.method == "POST":
        Form = NoteForm(request.POST)
        if Form.is_valid():
            note = Form.cleaned_data["note"]
            status = Form.cleaned_data["status"]
            Note.objects.create(content=note,status=status)
        return redirect("index")
    else:
        Form = NoteForm()

    notes = Note.objects.all()
    return render(request, "notes/index.html", {
        "notes": notes,
        "form": Form,
    })

