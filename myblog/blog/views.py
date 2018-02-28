from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView
# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name= "posts"
    paginate_by = 2
    template_name ="blog/post/list.html"

def post_detail(request,slug):
    # post = Post.objects.get(slug = slug)
    post = get_object_or_404(Post,slug = slug)
    return render(request,'blog/post/detail.html',{'post':post})
