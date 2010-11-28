from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from toosimplewiki.models import Article, Revision


def article_detail(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
		revision = article.revisions.all().order_by("-timestamp")[0]
	except Article.DoesNotExist:
		raise Http404
	return render_to_response("toosimplewiki/article_detail.html", {
		"article": article,
		"revision": revision,
	})
