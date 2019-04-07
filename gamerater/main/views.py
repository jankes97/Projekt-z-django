from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from .forms import GameForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def wszystkie_gry(request):
  text_views = "To jest text z views"
  gry = Game.objects.all()
  return render(request, 'lista_gier.html', {'text': text_views, 'gry': gry})

@login_required
def dodaj_gre(request):
  form = GameForm(request.POST or None, request.FILES or None)

  if form.is_valid():
    form.save()
    return redirect(wszystkie_gry)

  return render(request, 'gra_form.html', {'form': form})


@login_required
def edytuj_gre(request, id):
  gra = get_object_or_404(Game, pk=id)
  form = GameForm(request.POST or None, request.FILES or None, instance=gra)

  if form.is_valid():
    form.save()
    return redirect(wszystkie_gry)

  return render(request, 'gra_form.html', {'form': form})


@login_required
def usun_gre(request, id):
  gra = get_object_or_404(Game, pk=id)

  if request.method == 'POST':
    gra.delete()
    return redirect(wszystkie_gry)
  
  return render(request, 'potwierdz.html', {'gra': gra})
