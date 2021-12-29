from django.shortcuts import render
from .models import House
from .form import CommentForm
from django.views import generic

def homepage(request):
    estates = House.objects.all()
    contex={'estates': estates}
    return render(request, "core/homepage.html", contex)

def detail_page(request, pk):
    estates = House.objects.get(id=pk)
    form = CommentForm
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.house = House.objects.get(id=pk)
            form.save()
            context = {
                'estates': estates,
                "form": form,
            }
            return render(request, 'core/detail_page.html', context)
    context = {
        'estates': estates,
        "form": form,
    }
    return render(request, 'core/detail_page.html', context)

def post_comments(request, pk):
    estates = House.objects.get(id=pk)
    context={
        'estates': estates
    }
    return render(request, 'core/comments.html', context)

