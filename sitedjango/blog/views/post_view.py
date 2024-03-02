from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render

from ..models import Post

# class PostView(generic.View):
    # def get(self, request, *args, **kwargs):
        # return HttpResponse('Teste View')
        # return render(request, 'usuarios/home.html')

class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'