from django.db import models
from django.utils import timezone

class Blog(models.Model):
	title=models.CharField(max_length=600)
	description=models.TextField()
	created_by=models.CharField(max_length=100)
	created_date=models.DateTimeField(default=timezone.now)
	image=models.ImageField(upload_to='images/',blank=True,null=True)

	
	def __str__(self):
		return self.title




