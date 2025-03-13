from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='post_images/')
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200, unique=True)
    content = RichTextUploadingField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("more", kwargs={"slug": self.slug})
    
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
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Yil Daturi'
        verbose_name_plural = 'Yil Daturi'
        
#mmt bolimi

class Rahbar(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
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
    created_at = models.DateTimeField(auto_now_add=True)
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
    date = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Tarkibiy tuzilma'
        verbose_name_plural = 'Tarkibiy tuzilma'
        
class Qabul_Kunlari(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    day = models.CharField(max_length=150)
    time = models.CharField(max_length=150)
    lunch = models.CharField(max_length=150)
    def __str__(self):
        return self.day
    
class Bolim_Nizomi(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Bo'lim nizomi"
        verbose_name_plural = "Bo'lim nizomi"
        
class Principals(models.Model): #direktorlar
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='principal_photo/', null=True)
    phone_number = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    veb_sayt = models.TextField(blank=True, null=True)
    reception_days = models.TextField(null=True) #qabul kunlari
    date_of_birth = models.TextField(null=True)
    education = models.TextField(null=True)
    field = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    school_location = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("talim_muassa", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = "Ta'lim muassasalari"
        verbose_name_plural = "Ta'lim muassasalari"
        
class Talim_Tashkiloti(models.Model):
    name = models.CharField(max_length=200, null=True)
    content = RichTextUploadingField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Talim tashkiloti'
        verbose_name_plural = 'Talim tashkilotlari'
        
class Kun_Tartibi(models.Model):
    day = models.CharField(max_length=200)
    work_time = models.CharField(max_length=200)
    lunch_time = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.day
    
    class Meta:
        verbose_name = 'Kun tartibi'
        verbose_name_plural = 'Kun tartibi'
        
class Bosh_orinlar(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Bosh orin'
        verbose_name_plural = 'Bosh orinlar'
        
class Bolim_manzili(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Bo'lim manzili"
        verbose_name_plural = "Bo'lim manzili"
        
#oqituvchilarga
class Malaka_Oshirish(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='malaka_oshirish/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("malaka", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Malaka oshirish'
        verbose_name_plural = 'Malaka oshirish'
        
class Dars_Ishlanmalar(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='dars_ishlanmalari/', null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("dars-ishlanma", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Dars ishlanma'
        verbose_name_plural = 'Dars ishlanmalar'
        
class Fan_Testlar(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='oqituvchilarga/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("fan-test", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Fan test'
        verbose_name_plural = 'Fan testlar'
        
class Davlat_Dasturlari(models.Model):
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='davlat_dasturlari/', null=True, blank=True)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse("davlat_dastur", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Davlat dasturlari'
        verbose_name_plural = 'Davlat dasturlari'
        
class Talim_Qonun(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Talim qonun'
        verbose_name_plural = 'Talim qonun'
 
#oquvchilarga
        
class Imtihon_Materiallari(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)
    yil = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Imtihon materiallari'
        verbose_name_plural = 'Imtihon materiallari'
        
class Shahodatnomani_Tiklash(models.Model):
    title = models.TextField()
    content = RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Shahodatnomani tiklash'
        verbose_name_plural = 'Shahodatnomani tiklash'
        
#ota-onalarga
class Bogchaga_Joylashtirish(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Bog'chaga joylashtirish"
        verbose_name_plural = "Bog'chaga joylashtirish"
        
class Qabul_Teshirish(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Bog'chaga qabul navbatni teshirish"
        verbose_name_plural = "Bog'chaga qabul navbatni teshirish"
        
class Tolovlar_Malumot(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Bog'cha Tolovlar malumot"
        verbose_name_plural = "Bog'cha Tolovlar malumot"
        
class Birinchi_Sinf(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Birinchi sinf'
        verbose_name_plural = 'Birinchi sinf'
        
class Oquvchilar_Qabul(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Oquvchilarni maktabga qabul'
        verbose_name_plural = 'Oquvchilarni maktabga qabul'
        
class Bola_Kuchirish(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Bolani maktabdan kuchirish'
        verbose_name_plural = 'Bolani maktabdan kuchirish'
        
class Xorijiy_Fuqarolar(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Xorijiy fuqarolar'
        verbose_name_plural = 'Xorijiy fuqarolar'
        
#matbuot hizmati
class Video_Galereya(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    video = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='video_galereya_images/')
    
    def get_absolute_url(self):
        return reverse("video", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Video galereya'
        verbose_name_plural = 'Video galereya'
        
class Photo(models.Model):
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200, unique=True)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("foto", kwargs={"slug": self.slug})
    
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
     
# faoliyat

class Korrupsia_Qarshi(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='faoliyat/')
    
    def get_absolute_url(self):
        return reverse("korrupsia", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Korrupsiya qarshi'
        verbose_name_plural = 'Korrupsiya qarshi'
        
class Talim_Terminlar(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Talim terminlar'
        verbose_name_plural = 'Talim terminlar'
        
class Besh_Tashshabus(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='faoliyat')
    
    def get_absolute_url(self):
        return reverse("besh-tashabbus", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Besh tashshabus'
        verbose_name_plural = 'Besh tashshabus'
   
   
#normativ hujjatlar
        
class Prezident_Qarorlari(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='normativ_hujjatlar/', null=True, blank=True)
    content = RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Prezident qarorlari'
        verbose_name_plural = 'Prezident qarorlari'
    

class Hayat_Qarorlari(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Hayat qarorlari'
        verbose_name_plural = 'Hayat qarorlari'
        


class Meyoriy_Hujjatlar(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Me'yoriy hujjatlar"
        verbose_name_plural = "Me'yoriy hujjatlar"
        


class Tuman_Hujjatlari(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='normativ_hujjatlar/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    content = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("meyoriy-hujjat", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Tuman me'yoriy hujjatlar"
        verbose_name_plural = "Tuman me'yoriy hujjatlar"
    
    
#left sidebar uchun model

class LeftSidebar(models.Model):
    maktablar_soni = models.PositiveIntegerField()
    oquvchilar_soni = models.PositiveIntegerField()
    oqituvchilar_soni = models.PositiveIntegerField()
    
    def __str__(self):
        return "Left Sidebar"
    
    class Meta:
        verbose_name = "Maktablar Soni"
        verbose_name_plural = "Maktablar Soni"