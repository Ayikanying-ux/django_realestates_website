from django.shortcuts import render
from .models import House
from .form import CommentForm
from django.views import View
from django.db.models import Q

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

class AddLike(View):
    def post(self, request, pk, *args, **kwargs):
        form = CommentForm
        estates = House.objects.get(pk=pk)
        is_dislike = False

        for dislike in estates.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        is_like = False
        for like in estates.likes.all():
            if like == request.user:
                is_like == True
                break
        
        if not is_like:
            estates.likes.add(request.user)

        if is_like:
            estates.likes.remove(request.user)

        context = {
        'estates': estates,
        "form": form,
        }
        return render(request, 'core/detail_page.html', context)


class AddDislike(View):
    def post(self, request, pk, *args, **kwargs):
        estates = House.objects.get(pk=pk)
        form = CommentForm

        is_like = False

        for like in estates.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            estates.likes.remove(request.user)

        is_dislike = False

        for dislike in estates.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike: 
            estates.dislikes.add(request.user)
        
        if is_dislike:
            estates.dislikes.remove(request.user)
        context = {
        'estates': estates,
        "form": form,
        }
        return render(request, 'core/detail_page.html', context)


class Search(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        house = House.objects.filter(
            Q(name__icontains=query)
        )
        context = {"house": house}

        return render(request, 'core/search.html', context)



