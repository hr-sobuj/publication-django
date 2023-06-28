from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

import os
import uuid
import random

from datetime import datetime 

def book_directory_path(instance, filename):
    # Get Current Date
    todays_date = datetime.now()
    # print(str(todays_date.date()))
    path = "books/{}/".format(str(todays_date.date()))
    extension = "." + filename.split('.')[-1]
    stringId = str(uuid.uuid4())
    randInt = str(random.randint(10, 99))

    # Filename reformat
    filename_reformat = stringId + randInt + extension

    return os.path.join(path, filename_reformat)



class Book(models.Model):
    book_title = models.CharField(max_length = 5000,verbose_name="Book Title")
    writer = models.CharField(max_length = 5000,verbose_name="Writer")
    publisher = models.CharField(max_length = 5000,verbose_name="Publisher")
    quality = models.CharField(max_length = 5000,verbose_name="Quality")
    book_description = models.TextField(verbose_name="Book Description")
    total_page = models.IntegerField(
        default=0,
     )
    price = models.IntegerField(
        default=0,
     )
    discount = models.IntegerField(
        default=0,
     )
    
    main_cover = models.ImageField(upload_to=book_directory_path,verbose_name="Main Cover Image")
    book_cover1 = models.ImageField(upload_to=book_directory_path,verbose_name="Cover Image 1",blank=True, null=True)
    book_cover2 = models.ImageField(upload_to=book_directory_path,verbose_name="Cover Image 2",blank=True, null=True)
    book_cover3 = models.ImageField(upload_to=book_directory_path,verbose_name="Cover Image 3",blank=True, null=True)
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    class Meta:
        ordering=['-publish_date']

    def __str__(self):
        return self.book_title
    
