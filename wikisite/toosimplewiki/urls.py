from django.conf.urls.defaults import *
from django.views.generic import simple, list_detail
from toosimplewiki.models import Article, Revision
from toosimplewiki.views import article_detail, add_article


urlpatterns = patterns('',
    url(r'^$',
		simple.direct_to_template,
		{ "template": "home.html", },
		name="toosimplewiki_home"),

    url(r'^all/$',
		list_detail.object_list,
		{ "queryset": Article.objects.all(), },
		name="toosimplewiki_article_list"),

	url(r'^(?P<article_id>\d+)/$',
		article_detail,
		name="toosimplewiki_article_detail"),

	url(r'^new/$',
		add_article,
		name="toosimplewiki_add_article"),
)
