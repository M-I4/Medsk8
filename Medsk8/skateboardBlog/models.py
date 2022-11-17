from django.db import models
from accounts.models import Profile

# Create your models here.

class Post(models.Model):

    post_type_choices = models.TextChoices("Post Type", ["Article", "Opinion", "Review"])
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    content = models.TextField()
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return f"{self.title}, {self.publish_date}"


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    name = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
