from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    context = {"form": form}
    return render(request, 'authentication/register.html', context)
