from django.db import models

# Create your models here one by one.
    
class Studetails(models.Model):
    studentid = models.IntegerField()
    firstname = models.CharField(max_length = 500)
    lastname = models.CharField(max_length = 500)
    major = models.CharField(max_length = 150)
    year = models.CharField(max_length = 500)
    gpa = models.DecimalField(max_digits = 3, decimal_places = 2)

    
class information(models.Model):
    studentid = models.IntegerField()
    firstname = models.CharField(max_length = 500)
    lastname = models.CharField(max_length = 500)
    major = models.CharField(max_length = 150)
    year = models.CharField(max_length = 500)
    gpa = models.DecimalField(max_digits = 3, decimal_places = 2)

    
class studentinformation(models.Model):
    studentid = models.IntegerField()
    firstname = models.CharField(max_length = 500)
    lastname = models.CharField(max_length = 500)
    major = models.CharField(max_length = 150)
    year = models.CharField(max_length = 500)
    gpa = models.DecimalField(max_digits = 3, decimal_places = 2)
    
class bookinfo(models.Model):
    bookid = models.IntegerField()
    booktitle = models.CharField(max_length = 2000)
    authorname = models.CharField(max_length = 2000)
    currentlycheckedout = models.CharField(max_length = 10)
    numberoftimescheckedout = models.IntegerField()
    
class detailsbook(models.Model):
    bookid = models.IntegerField()
    booktitle = models.CharField(max_length = 2000)
    authorname = models.CharField(max_length = 2000)
    currentlycheckedout = models.CharField(max_length = 10)
    numberoftimescheckedout = models.IntegerField()
    
class books(models.Model):
    bookid = models.IntegerField()
    booktitle = models.CharField(max_length = 2000)
    authorname = models.CharField(max_length = 2000)
    currentlycheckedout = models.CharField(max_length = 10)
    numberoftimescheckedout = models.IntegerField()
    
class hellobooks(models.Model):
    bookid = models.IntegerField()
    booktitle = models.CharField(max_length = 2000)
    authorname = models.CharField(max_length = 2000)
    currentlycheckedout = models.CharField(max_length = 10)
    numberoftimescheckedout = models.IntegerField()
    
    
class knowbooks(models.Model):
    bookid = models.IntegerField()
    booktitle = models.CharField(max_length = 2000)
    authorname = models.CharField(max_length = 2000)
    currentlycheckedout = models.CharField(max_length = 10)
    numberoftimescheckedout = models.IntegerField()