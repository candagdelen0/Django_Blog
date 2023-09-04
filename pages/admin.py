from django.contrib import admin
from .models import Blog,Adviser, Slider

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("sehiradi","ulkeAdi")
    list_display_links = ("sehiradi",)


@admin.register(Adviser)
class AdviserAdmin(admin.ModelAdmin):
    list_display = ("baslik",)

admin.site.register(Slider)