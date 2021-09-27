from django.contrib import admin
from .models import Article,Comment,Contact


admin.site.register(Comment)
admin.site.register(Contact)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ["title","author","created_date"]#görüntü düzeneği
	list_display_links = ["title","created_date"]#tıklanabilir obj
	search_fields = ["title"]#başlağa göre ara
	list_filter = ["created_date"]#listeleriyor tarihe göre
	class Meta:
		model=Article
