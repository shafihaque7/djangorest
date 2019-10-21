from django.db import models

# Create your models here.
class Lead(models.Model):
   name = models.CharField(max_length=100)
   email = models.EmailField(max_length=100, unique=True)
   message = models.CharField(max_length=500, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   

class Salary(models.Model):
   name = models.CharField(max_length=100)
   salary = models.IntegerField()
   
class Paradigm(models.Model):
   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name
   
class Language(models.Model):
   name = models.CharField(max_length=50)
   paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

   def __str__(self):
      return self.name

class Programmer(models.Model):
   name = models.CharField(max_length=50)
   languages = models.ManyToManyField(Language)

   def __str__(self):
      return self.name