import markdown,re
from django.shortcuts import render,get_object_or_404
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
#from django.http import HttpResponse
from .models import Post, Category, Tag

# Create your views here.
def index(request):
    post_list = Post.objects.all()
#    return HttpResponse("欢迎访问我的博客首页！")
    return render(request, 'blog/index.html', context={'post_list':post_list})
#        'title': '我的博客首页',
#        'welcome': '欢迎访问我的博客首页'
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                      TocExtension(slugify=slugify),                                 ])
    post.body = md.convert(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>',md.toc,re.S)
    post.toc = m.group(1) if m is not None else ' '
    return render(request, 'blog/detail.html', context={'post': post})

#归档页面的视图函数
def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    )
    return render(request, 'blog/index.html', context={'post_list': post_list})
#分类页面的视图函数
def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})
#标签页面
def tag(request, pk):
    # 记得在开始部分导入 Tag 类
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t)
    return render(request, 'blog/index.html', context={'post_list': post_list})
