from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=False)
    
    def __str__(self):
        return self.title
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.content

    
    #models.OneToOneField 1대1참조
    #models.ManyToManyField 다대다 참조


    
