from datetime import datetime
from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=200, unique=True)

	def __unicode__ (self):
		return self.title


class Revision(models.Model):
	article = models.ForeignKey(Article, related_name="revisions")
	timestamp = models.DateTimeField(default=datetime.now())
	content = models.TextField()

	def __unicode__ (self):
		return "%s %s" % (self.timestamp.strftime("%s"), self.content)
