from django.shortcuts import render, get_object_or_404
# from blog.models import Post 
from .models import Post

# from django.views.generic import CreateView

# Create your views here.

def blog(request):
    """ A view to return the Blog Page """
    return render(request, "blog/blog.html")


def all_posts(request):
    """ A view to show all posts, including sorting and search queries """

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/posts.html', context)



def post_detail(request, post):
    """ A view to show individual post details """

    post = get_object_or_404(Post, slug=post, status='published')

    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)

# def add_post(request, user):
#     """ A function to create a blog post and 
#     render the add_blog page """

    
# def PostDetailView(DetailView):
#     model = Post


    #<app>/<model>_<viewtype>.html
