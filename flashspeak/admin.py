from django.contrib import admin

from .models import Deck, Card, Language

admin.site.register(Deck)
admin.site.register(Card)
admin.site.register(Language)