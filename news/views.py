from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import  Article, Feed
from .forms import FeedForm

from django.utils import timezone
import feedparser, datetime
from .tasks import  save_article

from django.core.cache.backends.base import DEFAULT_TIMEOUT

from django.views.decorators.cache import cache_page
from django.conf import settings
#from rssfeed.settings import display_list
from clips.views import get_videos


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

"""
def index(request):
    return render (request, 'base.html' , {})
"""
#@cache_page(CACHE_TTL)
def index(request):
    display_list = Article.objects.articles_after(days=10)
    #rowsd = [display_list[x:x+1] for x in range(0, len(display_list), 1)]
    videos = get_videos()

    paginator = Paginator(display_list, 15)
    page = request.GET.get('page')

    video_paginator = Paginator(videos, 10)
    try:
        rows = paginator.page(page)
        vid = video_paginator.page(page)
    except PageNotAnInteger:
        rows = paginator.page(1)
        vid = video_paginator.page(1)

    except EmptyPage:
        rows = paginator.page(paginator.num_pages)
        vid = video_paginator.page(video_paginator.num_pages)


    context = {'rows' : rows, 'vid': vid}
    return render (request, 'news/articles_list.html' , context)


@cache_page(CACHE_TTL)
def feeds_list(request):
    feeds = Feed.objects.all()
    return render(request, 'news/feeds_list.html', {'feeds': feeds})
