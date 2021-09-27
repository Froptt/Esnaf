from django.db import models
from ckeditor.fields import RichTextField


# modeler burda oluşucak
class Article(models.Model):
	author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
	title = models.CharField(max_length=50, verbose_name="Başlık")
	content = RichTextField(verbose_name="Konu")
	created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
	article_image = models.FileField(blank=True, null=True, verbose_name="Resim Ekle")
	
	def __str__(self):
		return f" Yazar {self.author} - Başlık {self.title}"
	
	class Meta:
		ordering = ['-created_date']  # tersen sıralıyor


class Contact(models.Model):
	name = models.CharField(max_length=16,verbose_name="İsim")
	email = models.EmailField()
	phone = models.CharField(max_length=11,verbose_name="Telefon")
	message = models.TextField(verbose_name="Mesaj")
	
	def __str__(self):
		return self.name


class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
	comment_author = models.CharField(max_length=50, verbose_name="İsim")
	comment_content = models.CharField(max_length=200, verbose_name="Yorum")
	comment_date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.comment_content
	
	class Meta:
		ordering = ['-comment_date']
