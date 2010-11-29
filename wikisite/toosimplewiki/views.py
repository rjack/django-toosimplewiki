from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, loader
from toosimplewiki.forms import ArticleForm, RevisionForm
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


# TODO
# http://bit.ly/gfPFgy
# http://bit.ly/gOkXdK
def add_article(request):
	if request.method == "GET":
		article_form = ArticleForm()
		revision_form = RevisionForm()
	elif request.method == "POST":
		article_form = ArticleForm(request.POST)
		revision_form = RevisionForm(request.POST)

		if article_form.is_valid() and revision_form.is_valid():
			new_article = article_form.save()
			new_revision = revision_form.save(commit=False)
			new_revision.article = new_article
			new_revision.save()
			return HttpResponseRedirect(reverse("toosimplewiki_article_detail",
				args=(new_article.id,)))

	return render_to_response("toosimplewiki/add_article_form.html", {
		"article_form": article_form,
		"revision_form": revision_form,
	}, context_instance=RequestContext(request))
