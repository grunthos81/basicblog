from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

class Section(models.Model):
    section_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.section_name

class Article(models.Model):
    title = models.CharField(max_length=60)
    subtext = models.CharField(max_length=108)
    permalink = models.CharField(max_length=40, unique=True, blank=False)
    body = RichTextField(blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=False)
    draft = models.BooleanField(default=True, blank=False)
    last_edited = models.DateTimeField(default=datetime.now())
    image = models.URLField(default='https://i.imgur.com/PdQAt6.jpg', blank=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-last_edited']
    





