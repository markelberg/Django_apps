from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age} años"
