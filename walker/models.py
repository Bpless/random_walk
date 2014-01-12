from django.db import models


class Trial(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
