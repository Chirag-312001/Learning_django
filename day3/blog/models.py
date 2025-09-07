from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author_name = models.ForeignKey(Author,models.CASCADE,related_name='posts')

    def __str__(self):
        return f"{self.title}===={self.content}"

class Comments(models.Model):
    post = models.ForeignKey(Posts,models.CASCADE,related_name='posts')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'comment on {self.post.title}'
    


