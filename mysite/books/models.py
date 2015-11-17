from django.db import models
from django.contrib import admin

class Author(models.Model):
    AuthorID = models.IntegerField()
    Name = models.CharField(max_length = 50)
    Age = models.FloatField()
    Country = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.Name

class Book(models.Model):
    ISBN = models.IntegerField()
    Title = models.CharField(max_length = 100)
    Author = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 50)
    PublishDate = models.DateField()
    Price = models.FloatField()

admin.site.register(Author)
admin.site.register(Book)