from django.shortcuts import render,redirect,get_object_or_404,reverse
from .forms import ArticleFrom
from .forms import Article,Comment,ContactForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
def articles(request):
	keyword=request.GET.get("keyword")
	if keyword:
		articles=Article.objects.filter(title__contains = keyword)
		return render(request,"articles.html",{"articles" : articles})
	articles = Article.objects.all()
	
	return render(request,"articles.html",{"articles":articles})
	
def index(request):
	
	return render(request,"index.html")

def about(request):
	return render(request,"about.html")

def emailView(request):
	if request.method=="POST":
		form=ContactForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data["name"]
			email=form.cleaned_data["email"]
			phone=form.cleaned_data["phone"]
			message=form.cleaned_data["message"]
			form.save()
			messages.success(request,"Mesaj Başarılı bir şekilde Gönderildi.")
			return redirect("index")
	else:
		form=ContactForm()
	return render(request,"contact.html",{"form":form})















@login_required
def dashboard(request):
	articles=Article.objects.filter(author=request.user)
	content={
		"articles":articles
	}
	return render(request,"dashboard.html",content)
@login_required(login_url = "user:login")
def addarticle(request):
	form=ArticleFrom(request.POST or None , request.FILES or None)
	if form.is_valid():
		article=form.save(commit=False)
		article.author=request.user
		article.save()
		messages.success(request,"Makale Başarılı Bir şekilde Oluşturuldu.")
		return redirect("article:dashboard")
	return render(request,"addarticle.html",{
		"form":form
	})
def detail(request,id):
	# article=Article.objects.filter(id=id).first()
	article=get_object_or_404(Article,id=id)
	comments=article.comments.all()
	return render(request,"detail.html",{"article":article,"comments":comments})




@login_required(login_url = "user:login")
def updateArticle(request,id):
	article=get_object_or_404(Article,id=id)
	form=ArticleFrom(request.POST or None,request.FILES or None,instance=article)
	if form.is_valid():
		article = form.save(commit=False)
		article.author = request.user
		article.save()
		messages.success(request, "Makale Başarılı Bir şekilde Güncellendi.")
		return redirect("article:dashboard")
	return render(request,"update.html",{"form":form})
@login_required(login_url = "user:login")
def deleteArticle(request,id):
	article=get_object_or_404(Article,id=id)
	article.delete()
	messages.success(request, "Makale Başarılı Bir şekilde Silindi.")
	return redirect("article:dashboard")

def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))
