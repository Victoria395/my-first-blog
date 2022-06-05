from django.db import models
from django.conf import settings


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	text = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, blank=True)

	def __str__(self):
		return self.title

