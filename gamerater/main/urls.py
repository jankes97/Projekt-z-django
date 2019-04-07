from django.urls import path
from .views import wszystkie_gry, dodaj_gre, edytuj_gre, usun_gre

urlpatterns = [
    path('gry/', wszystkie_gry, name='wszystkie_gry'),
    path('dodaj/', dodaj_gre, name='dodaj_gre'),
    path('edytuj/<int:id>/', edytuj_gre, name='edytuj_gre'),
    path('usun/<int:id>/', usun_gre, name='usun_gre'),
]
