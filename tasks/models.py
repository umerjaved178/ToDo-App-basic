from django.db import models

# Create your models here.
class Taskfield(models.Model):
	"""docstring for ClassName"""

	task=models.CharField(max_length=200)
	complete=models.BooleanField(default=False)

	def __str__(self):
		return f"{self.task}"

