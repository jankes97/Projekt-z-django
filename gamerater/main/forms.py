from django.forms import ModelForm
from .models import Game


class GameForm(ModelForm):
  class Meta:
    model = Game
    fields = ['name', 'platform', 'year', 'released', 'description', 'metacritic_rating', 'photo']
