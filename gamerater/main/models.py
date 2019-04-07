from django.db import models

# Create your models here.

class Game(models.Model):
  name = models.CharField(max_length=128)
  platform = models.CharField(default="", max_length=40)
  year = models.IntegerField(null=True, blank=True)
  released = models.DateField(null=True, blank=True)
  description = models.TextField(default="")
  metacritic_rating = models.DecimalField(null=True, blank=True, decimal_places=7, max_digits=10)
  photo = models.ImageField(null=True, blank=True, upload_to='okladka')
  

  def __str__(self):
    return self.name_with_platform()

  def name_with_platform(self):
    return str(self.name) + " (" + self.platform + ")"

    

