from django.db import models
from django.utils.text import slugify

from user_profile.models import User
from .slugs import generate_unique_slug
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Blog(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_blogs',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        related_name='category_blogs',
        on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='tag_blogs',
        blank=True
    )
    likes = models.ManyToManyField( 
        User,
        related_name='user_likes',
        blank=True
    )
    title = models.CharField(
        max_length=250
    )
    slug = models.SlugField(null=True, blank=True)
    banner = models.ImageField(upload_to='blog_banners')
    description = RichTextUploadingField()
    created_date = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    #from Video here
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        updating = self.pk is not None
        
        if updating:
            self.slug = generate_unique_slug(self, self.title, update=True)
            super().save(*args, **kwargs)
        else:
            self.slug = generate_unique_slug(self, self.title)
            super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_comments',
        on_delete=models.CASCADE
    )
    blog = models.ForeignKey(
        Blog,
        related_name='blog_comments',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text


class Reply(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_replies',
        on_delete=models.CASCADE
    )
    comment = models.ForeignKey(
        Comment,
        related_name='comment_replies',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
    
    
class Sell_Post_Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
# Create your models here.


class Sell_post(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_sell_post',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Sell_Post_Category,
        related_name='category_sell_post',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=250
    )
    slug = models.SlugField(null=True, blank=True)
    banner = models.ImageField(upload_to='sell_banners')
    description = RichTextUploadingField()
    created_date = models.DateField(auto_now_add=True)

    #from Video here
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        updating = self.pk is not None
        
        if updating:
            self.slug = generate_unique_slug(self, self.title, update=True)
            super().save(*args, **kwargs)
        else:
            self.slug = generate_unique_slug(self, self.title)
            super().save(*args, **kwargs)