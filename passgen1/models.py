from django.db import models

# Create your models here.

class Userpass(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_password = models.CharField(max_length=500)

	def __int__(self):
		return self.user_id
