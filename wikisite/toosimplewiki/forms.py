from django import forms
from django.forms.formsets import formset_factory
from toosimplewiki.models import Article, Revision


class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article


class RevisionForm(forms.ModelForm):
	class Meta:
		model = Revision
		exclude = ('timestamp', 'article')
