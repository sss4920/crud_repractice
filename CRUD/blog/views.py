from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def main(request):
    articles= Article.objects.all()#article들의 모음집 생성
    return render(request, "blog/main.html", {"articles":articles})

def new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.title = form.cleaned_data["title"]
            article.content = form.cleaned_data["content"]
            article.published_at = timezone.now()
            article.save()
            return redirect("blog:main")
    else:#이게 get
        form = ArticleForm()
        return render(request, "blog/new.html", {'form':form})

def detail(request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.method == "POST":
                form = CommentForm(request.POST)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.article = article
                        comment.content = form.cleaned_data["content"]
                        comment.save()
                        return redirect("blog:detail", article_id)
        else:
                form = CommentForm() 
                return render(request, "blog/detail.html", {"article":article, "form":form})

def edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.title = form.cleaned_data["title"]
            article.content = form.cleaned_data["content"]
            article.published_at = timezone.now()
            article.save()
            return redirect("blog:detail", article.id)
    else:
        form = ArticleForm(instance=article)
        return render(request, "blog/new.html", {'form':form})
def delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect("blog:main")


def comment_delete(request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return redirect("blog:detail", comment.article.id)

def comment_edit(request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.method == "POST":
                form = CommentForm(request.POST, instance=comment)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.content = form.cleaned_data["content"]
                        comment.save()
                        return redirect("blog:detail", comment.article.id)
        else:
                form = CommentForm(instance=comment)
                return render(request, "blog/new.html", {"form": form})
# article_id도 받아서 바로 다이렉트 할때만 써도 되고
# delete 했을 때 객체만 지워주니 이런것도 가능
#
#def comment_delete(request, comment_id):
#       comment = get_object_or_404(Comment, id=comment_id)
#       comment.delete()
#       return redirect("blog:detail", comment.article.id) 
#
#    
#         
#def comment_delete(request, article_id, comment_id):
#        comment = get_object_or_404(Comment, id=comment_id)
#        comment.delete()
#        return redirect("blog:detail", article_id)
#
#
#