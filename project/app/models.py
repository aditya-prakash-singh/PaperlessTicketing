from django.db import models

# Create your models here.
class Ticket(models.Model):
	fname=models.CharField(max_length=22)
	lname=models.CharField(max_length=22)
	email=models.CharField(max_length=122)
	phone=models.CharField(max_length=13)
	dat=models.CharField(max_length=13)
	id_no=models.CharField(max_length=122)
	def __str__(self):
		return self.fname