from django.http import HttpResponse
from django.shortcuts import render_to_response
from toosimplewiki.models import Article, Revision


def article_detail(request, article_id):
	article = Article.objects.filter(pk=article_id)[0]
	revision = article.revisions.all().order_by("-timestamp")[0]
	return render_to_response("toosimplewiki/article_detail.html", {
		"article": article,
		"revision": revision,
	})
