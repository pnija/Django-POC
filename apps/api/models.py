from django.db import models

class Animal(models.Model):
    unique_id = models.IntegerField(unique=True, default=0)
    name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.unique_id)

class Herd(models.Model):
    animals = models.ManyToManyField(Animal, related_name='get_herds')

    def __str__(self):
        return str(self.id)

class AnimalWeight(models.Model):
    
    weight = models.FloatField()
    animals = models.ForeignKey(Animal, related_name='get_animal', on_delete=models.CASCADE)
    weight_date = models.DateTimeField()

    def __str__(self):
        return str(self.id)


    
