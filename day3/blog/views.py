from django.shortcuts import render

# Create your views here.
from .models import Posts

def post_list(request):
    posts = Posts.objects.all().order_by('created_at')
    return render(request,'blog/post_list.html',{'posts':posts})

from django.views.generic import ListView


class PostListView(ListView):
    model = Posts
    template_name = 'blog/post_list.html'
    context_object_name ='posts'
    ordering = ['-created_at']


