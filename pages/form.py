from django import forms
from django.forms import TextInput, Textarea
from pages.models import Blog, Adviser


class TextCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('sehiradi','ulkeAdi','image','aciklama','metin')
        labels = {
            'sehiradi' : 'Şehir Adı',
            'ulkeAdi': 'Ülke Adı',
            'aciklama': 'Yazı Özeti',
            'metin': 'Seyahat Yazısı Metni'
        }
        widgets = {
            "sehiradi": TextInput(attrs={"class":"form-control"}),
            "ulkeAdi": TextInput(attrs={"class":"form-control"}),
            "aciklama": TextInput(attrs={"class": "form-control"}),
            "metin": Textarea(attrs={"class": "form-control"}),
        }
        error_messages = {
            "sehiradi": {
                "required":"Şehir Adını Girmelisiniz",
                "max_lenght":"Maksimum 50 karakter girebilirsiniz"
            },
            "ulkeAdi": {
                "required": "Ülke Adını Girmelisiniz",
                "max_lenght": "Maksimum 100 karakter girebilirsiniz"
            },
            "aciklama": {
                "required": "Açıklama Girmelisiniz",
                "max_lenght": "Maksimum 255 karakter girebilirsiniz"
            },
            "metin": {
                "required": "Metin Yazısını Girmelisiniz"
            }
        }