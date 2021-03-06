# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
#from .models_properties.website_post_properties import CATEGORIES

CATEGORIES = (
        ("wydarzenia", "wydarzenia"),
        ("informacje", "informacje"),
        ("konkursy", "konkursy"),
        ("wycieczki", "wycieczki"),
        ("sport", "sport"),)



class WebsitePost(models.Model):
    content = RichTextUploadingField()
    date = models.DateField(auto_now_add=True, blank=True)
    author = models.CharField(max_length=150, blank=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=120, choices=CATEGORIES)

    image = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'wpis'
        verbose_name_plural = 'Wpisy'


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'galeria'
        verbose_name_plural = "Galerie"


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='image_in_gallery')
    image = models.ImageField(upload_to='gallery/%Y/%m/%d')
    title = models.CharField(max_length=200, null=True)

    def __str__(self):
        return 'blabla'

    class Meta:
        verbose_name = 'zdjęcie'
        verbose_name_plural = "Zdjęcia"
