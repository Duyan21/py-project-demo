from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django import forms

from notes.models import Note

# Create your views here.


class NoteForm(forms.Form):
    note = forms.CharField(max_length=100)
    status = forms.BooleanField(required=False)


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))

def index(request):
    if request.method == "POST":
        Form = NoteForm(request.POST)
        if Form.is_valid():
            user = request.user
            note = Form.cleaned_data["note"]
            status = Form.cleaned_data["status"]
            Note.objects.create(user=user, content=note, status=status)
        return redirect("index")
    else:
        Form = NoteForm()

    notes = Note.objects.filter(user=request.user)
    return render(request, "notes/index.html", {
        "notes": notes,
        "form": Form,
    })


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("index")
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()

    return render(request, "notes/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")