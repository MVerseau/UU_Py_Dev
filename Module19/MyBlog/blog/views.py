from django.shortcuts import render
from .models import Post
from .forms import PostsPerPage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def load_posts_number(form):
    if form.is_valid():
        number = form.cleaned_data['number']
    return number


def post_list(request):
    template_name = 'index.html'
    number = 3
    form = PostsPerPage(request.POST)
    if request.method == 'POST':
        number = load_posts_number(form)
    object_list = Post.objects.all()
    paginator = Paginator(object_list, number)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger as e:
        # print(e)
        posts = paginator.page(1)
    except EmptyPage as e:
        # print(e)
        posts = paginator.page(paginator.num_pages)
    context = {
        'page': page,
        'posts': posts,
        'title': 'MyBlog',
        'paginator': paginator,
        'form': form,
        # 'func':func
    }
    return render(request, template_name, context)
