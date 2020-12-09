from .models import *
from django.views.generic import View
from .utils import *
from .forms import *
from django.shortcuts import redirect


# Create your views here.
class PostList(ObjectListMixin, View):
    model = Post
    template = 'blog/index.html'


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagList(ObjectListMixin, View):
    model = Tag
    template = 'blog/tags_list.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'
    url = 'tags_list_url'


class TagUpdate(View):
    def gen(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(instance=tag)
        return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'
    url = 'posts_list_url'
