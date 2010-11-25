from django.contrib import admin
from toosimplewiki.models import Article, Revision

class RevisionsInline(admin.TabularInline):
	model = Revision
	extra = 1


class ArticleAdmin(admin.ModelAdmin):
	inlines = [RevisionsInline]


admin.site.register(Article, ArticleAdmin)
