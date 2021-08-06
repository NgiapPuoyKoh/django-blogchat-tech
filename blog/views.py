from django.conf.urls import url
from django.shortcuts import render, get_object_or_404, redirect
# from blog.models import Post 
from .models import Post
from django.views.generic.edit import CreateView
from django.urls import reverse


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


class PostCreateView(CreateView):
    model = Post

    fields = [
        'title',
        'excerpt',
        'content',
        'topic',
        'status'
        # 'slug'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        # form.instance.slug = slugify(self.post.title)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('post_detail', kwargs={'slug': self.post})

# def add_post(request, user):
#     """ A function to create a blog post and 
#     render the add_blog page "
    
# def PostDetailView(DetailView):
#     model = Post


#<app>/<model>_<viewtype>.html