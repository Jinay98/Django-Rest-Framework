from django.db import models

# Create your models here.
class Paradigm(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


#Language model is dependent on paradigm model so we write that above this one also while entering info we need to first fill data in paradigm
class Language(models.Model):
    name=models.CharField(max_length=50)
    paradigm=models.ForeignKey(Paradigm,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name=models.CharField(max_length=50)
    languages=models.ManyToManyField(Language)

    def __str__(self):
        return self.name