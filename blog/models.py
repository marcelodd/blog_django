from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
	#id   = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100, blank=False)
	
	def __unicode__(self):
		return u'%s' % self.name

class Post(models.Model):
	#id    = models.AutoField(primary_key=True)
	title    = models.CharField(max_length=100, blank=False)
	text     = models.TextField(blank=False)
	date     = models.DateTimeField(auto_now=True)
	slug     = models.SlugField(blank=False)
	category = models.ForeignKey(Category,
        on_delete=models.CASCADE, default=0)
	
	def __unicode__(self):
		return u'%s' % self.title

	
