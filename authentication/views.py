from django.contrib.auth import login
from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    context = {"form": form}
    return render(request, 'authentication/register.html', context)