from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager,self).get_queryset().filter(status = 'published')

class Post(models.Model):
    def get_absolute_url(self):
        return self.slug
    STATUS_CHOICES = (
        ('drafts','Drafts'),
        ('published','Published'),
    )
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length=100,unique_for_date = 'publish')
    author = models.ForeignKey(User,on_delete = models.CASCADE,related_name= 'blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length= 10, choices = STATUS_CHOICES, default = 'drafts')
    published = PublishManager()
