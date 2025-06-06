from django.db import models
from django.contrib.auth.models import User

# creating Post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # string representation
    def __str__(self):
        return self.title