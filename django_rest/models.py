from django.db import models

# Create your models here.
class Student(models.Model):
  st_id=models.IntegerField(primary_key=True)
  st_name=models.CharField(max_length=50)
  st_email=models.EmailField()
  st_address=models.CharField(max_length=100)
  st_class=models.CharField(max_length=10)

  def __str__(self):
    return self.st_name
  
class Category(models.Model):
  category=models.CharField(max_length=50)

  def __str__(self):
    return self.category

class Book(models.Model):
  category=models.ForeignKey(Category,on_delete=models.CASCADE)
  book_id=models.IntegerField(primary_key=True)
  book_name=models.CharField(max_length=50)
  book_price=models.FloatField(max_length=100)

  def __str__(self):
    return self.book_name
