from django.db import models
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    if value.file.content_type != 'application/pdf':
        raise ValidationError('File format not Supported!!!!')


class Career(models.Model):
	



	firstname        = models.CharField(max_length=200)
	lastname         = models.CharField(max_length=250)
	phone            = models.CharField(max_length=100)
	email            = models.EmailField(max_length=255)
	location         = models.CharField(max_length=255)
	education        = models.CharField(max_length=255)
	cv               = models.FileField(upload_to='documents/CVs/', validators=[validate_file_extension])
	career_objective = models.TextField()
	uploaded_at      = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email


