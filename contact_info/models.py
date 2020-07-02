from django.db import models
# Create your models here.

class ContactInfo(models.Model):

	name = models.CharField(max_length = 100)
	submitted_time = models.DateField()
	location = models.CharField(max_length = 100)
	city = models.CharField(max_length = 100)


	def __str__(self):
		return self.name



