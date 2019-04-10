from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Games #importowanie z models.py tabeli Games
from .forms import GameForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def wszystkie_gry(request):
  text_views = "To jest text z views"
  gry = Games.objects.all() #wyświetlanie gier z bazy danych  
  return render(request, 'lista_gier.html', {'text': text_views, 'gry': gry})

@login_required
def dodaj_gre(request):
  form = GameForm(request.POST or None, request.FILES or None) #Podajemy wszystkie dane jeśli nie to użyjemy None = puste

  if form.is_valid():
    form.save() #jeśli nie ma błędów to zapisz
    return redirect(wszystkie_gry) #powykonaniu zadania powrót na do strony głownej 

  return render(request, 'gra_form.html', {'form': form})

@login_required
def edytuj_gre(request, id):
  gra = get_object_or_404(Games, pk=id) #próbujemy pobrać dane na postarwie id, jesli nie ma takiego id to bład 404
  form = GameForm(request.POST or None, request.FILES or None, instance=gra) #przekazanie danych z bazy do form by wypełnić dane

  if form.is_valid():
    form.save()
    return redirect(wszystkie_gry)

  return render(request, 'gra_form.html', {'form': form})

@login_required
def usun_gre(request, id):
  gra = get_object_or_404(Games, pk=id)

  if request.method == 'POST':
    gra.delete()
    return redirect(wszystkie_gry)
  
  return render(request, 'potwierdz.html', {'gra': gra})
