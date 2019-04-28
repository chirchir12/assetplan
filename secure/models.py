from django.db import models

class Contact(models.Model):
	fullname = models.CharField(max_length=250)
	email    = models.EmailField()
	phone    = models.CharField(max_length=100)
	message  = models.TextField()

	def __str__(self):
		return self.email



