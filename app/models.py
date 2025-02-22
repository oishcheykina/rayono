from django.db import models
from django.urls import reverse
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
     
#akani rasmi           
class Boss(models.Model):
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Rahbar'
        verbose_name_plural = 'Rahbar'
    
class Yil_Dasturi(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Yil Daturi'
        verbose_name_plural = 'Yil Daturi'
        
#mmt bolimi

class Rahbar(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    field = models.TextField() #kto eto
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    faks = models.TextField()
    vebsayt = models.TextField()
    tarjima_xol = RichTextUploadingField(null=True, blank=True)
    majburiyatlari = RichTextUploadingField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Rahbar'
        verbose_name_plural = 'Rahbariyat'

class Apparat_Xodimi(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    field = models.TextField() #kto eto
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    faks = models.TextField()
    vebsayt = models.TextField()
    tarjima_xol = RichTextUploadingField(null=True, blank=True)
    majburiyatlari = RichTextUploadingField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Apparat hodimi'
        verbose_name_plural = 'Apparat Hodimlari'
        
class Tarkibiy_Tuzilma(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Tarkibiy tuzilma'
        verbose_name_plural = 'Tarkibiy tuzilma'
        
class Qabul_Kunlari(models.Model):
    date = models.DateTimeField(auto_now=True)
    day = models.CharField(max_length=150)
    time = models.CharField(max_length=150)
    lunch = models.CharField(max_length=150)
    def __str__(self):
        return self.day
    
class Bolim_Nizomi(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Bo'lim nizomi"
        verbose_name_plural = "Bo'lim nizomi"
        
class Principals(models.Model): #direktorlar
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='principal_photo/', null=True)
    phone_number = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    veb_sayt = models.TextField(blank=True, null=True)
    reception_days = models.TextField(null=True) #qabul kunlari
    date_of_birth = models.TextField(null=True)
    education = models.TextField(null=True)
    field = models.TextField(null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse("more", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Direktor'
        verbose_name_plural = 'Direktorlar'
        
class Talim_Tashkiloti(models.Model):
    name = models.CharField(max_length=200, null=True)
    content = RichTextUploadingField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Talim tashkiloti'
        verbose_name_plural = 'Talim tashkilotlari'
        
class Kun_Tartibi(models.Model):
    day = models.CharField(max_length=200)
    work_time = models.CharField(max_length=200)
    lunch_time = models.CharField(max_length=200)
    
    def __str__(self):
        return self.day
    
    class Meta:
        verbose_name = 'Kun tartibi'
        verbose_name_plural = 'Kun tartibi'
        
class Bosh_orinlar(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Bosh orin'
        verbose_name_plural = 'Bosh orinlar'
        
class Bolim_manzili(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Bo'lim manzili"
        verbose_name_plural = "Bo'lim manzili"