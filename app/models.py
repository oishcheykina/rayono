from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    image = models.ImageField(upload_to='post_images/')
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200, unique=True)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("more", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Сохраняем новый пост

        # Проверяем количество постов
        if Post.objects.count() > 100:
            oldest = Post.objects.order_by('created_at').first()  # Самый старый пост
            if oldest:
                oldest.delete()
                
class Announcement(models.Model):
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200, unique=True)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("announcement", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = "E'lon"
        verbose_name_plural = "E'lonlar"
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Сохраняем новый пост

        # Проверяем количество постов
        if Announcement.objects.count() > 100:
            oldest = Announcement.objects.order_by('created_at').first()  # Самый старый пост
            if oldest:
                oldest.delete()
                
class Photo(models.Model):
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200, unique=True)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("announcement", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotogalereya'
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Сохраняем новый пост

        # Проверяем количество постов
        if Photo.objects.count() > 100:
            oldest = Photo.objects.order_by('created_at').first()  # Самый старый пост
            if oldest:
                oldest.delete()