# Generated by Django 4.2.4 on 2023-08-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adviser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=100)),
                ('aciklama', models.CharField(max_length=255)),
                ('metin', models.TextField()),
            ],
        ),
    ]