from django.shortcuts import render
from .models import House

def homepage(request):
    estates = House.objects.all()
    contex={'estates': estates}
    return render(request, "core/homepage.html", contex)

def detail_page(request, pk):
    estates = House.objects.get(id=pk)
    context = {'estates': estates}
    return render(request, 'core/detail_page.html', context)

def comments(request, pk):
    estates = House.objects.get(id=pk)
    context={
        'estates': estates
    }
    return render(request, 'core/comments.html', context)
