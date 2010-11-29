from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from toosimplewiki.models import Article, Revision
from toosimplewiki.forms import ArticleForm, RevisionForm


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


# TODO
# http://bit.ly/gfPFgy
# http://bit.ly/gOkXdK
def new_article(request):
	if request.method == 'POST':
		article_form = ArticleForm(request.POST)
		revision_form = RevisionForm(request.POST)
