from django import forms
from django.forms import ModelForm
from .models import *

class ArticleForm(ModelForm):
	class Meta:
		model=Taskfield
		fields='__all__'