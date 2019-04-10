from django.db import models

# Create your models here.

class ExtraInfo(models.Model):
  RODZAJE = {
    (0, 'Nieznany'),
    (1, 'Sci-Fi'),
    (2, 'Horrot'),
    (3, 'FirstPersonShooter'),
    (4, 'Indie')
  }
  rodzaj = models.IntegerField(default=0, choices=RODZAJE) #choices -> przechowuej tylko liczby z RODZAJE

  def __str__(self):
    return self.rodzja_name()

  def rodzja_name(self):
    return str(self.rodzaj)

class Games(models.Model):
  name = models.CharField(max_length=128) #string o długości 128 znaków
  platform = models.CharField(default="", max_length=40)
  description = models.TextField(default="") #string z większą ilością znaków / default="" 
  year = models.IntegerField(null=True, blank=True) #Pole z liczbą
  released = models.DateField(null=True, blank=True) #Pole z datą / null=true: pole nie jest wymagane
  rating = models.DecimalField(null=True, blank=True, decimal_places=7, max_digits=10) #wartość liczbowa z przecinkiem
  photo = models.ImageField(null=True, blank=True, upload_to='okladka') #dodawanie zdjęcia
  info = models.OneToOneField(ExtraInfo, on_delete=models.CASCADE, primary_key=True) #on_delete=models.CASCADE -> jeśli element z bd zostanie usunięty to ten drugi obiekt z bazy danych

  def __str__(self):
    return self.name_with_year()

  def name_with_year(self):
    return str(self.name) + " (" + str(self.platform) + ")"

class Review(models.Model):
  text = models.CharField(default='', blank=True, max_length=128)
  stars = models.IntegerField(default=5)
  games = models.ForeignKey(Games, on_delete=models.CASCADE)
  #python3 manage.py makemigrations
  #python3 manage.py migrate

  def __str__(self):
    return self.text
  

class Studio(models.Model):
  nazwa = models.CharField(max_length=128)
  kraj = models.CharField(max_length=128)
  gry = models.ManyToManyField(Games)
  #python3 manage.py makemigrations
  #python3 manage.py migrate
  
  def __str__(self):
    return self.nazwa