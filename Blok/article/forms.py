from django import forms
from .models import Article, Comment, Contact


class ArticleFrom(forms.ModelForm):
	class Meta:
		model = Article
		fields = ["title", "content", "article_image"]


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ["name", "email", "phone", "message"]



