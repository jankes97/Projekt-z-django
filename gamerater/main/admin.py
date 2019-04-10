from django.contrib import admin
from .models import Games
from .models import ExtraInfo, Review, Studio

# Register your models here.

@admin.register(Games)
class GameAdmin(admin.ModelAdmin):
  #field = ('name', 'description')
  list_display = ('name', 'platform', 'rating', 'released')
  list_filter = ('platform', 'year', 'released')
  search_fields = ('name', 'description')


#admin.site.register(Games)

admin.site.register(ExtraInfo)
admin.site.register(Review)
admin.site.register(Studio)
