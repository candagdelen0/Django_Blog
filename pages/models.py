from django.db import models

class Blog(models.Model):
    sehiradi = models.CharField(max_length=50)
    ulkeAdi = models.CharField(max_length=100)
    sehirResmi = models.CharField(max_length=100)
    aciklama = models.CharField(max_length=255)
    metin = models.TextField()
    
    def __str__(self):
        return  f"{self.sehiradi} - {self.ulkeAdi}"

class Adviser(models.Model):
    baslik = models.CharField(max_length=100)
    aciklama = models.CharField(max_length=255)
    metin = models.TextField()
    resim = models.CharField(max_length=100, default="10.jpg")

    def __str__(self):
        return f"{self.baslik}"
    
class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    text = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title}"