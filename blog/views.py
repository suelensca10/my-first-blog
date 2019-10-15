from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    #A variável posts é o nome do queryset que faz esse filtro abaixo. Quando precisar pode se referenciar a ele por esse nome
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})