from django.db import models
class Employee(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextField()
    jobrole = models.CharField(max_length=200)
    def __str__(self):
        return self.name