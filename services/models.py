from django.db import models

class Quote(models.Model):
	fname    = models.CharField(max_length=250)
	phone    = models.CharField(max_length=100)
	email    = models.EmailField(max_length=250, null=True, blank=True)
	message  = models.TextField()

	def __str__(self):
		return self.fname
