from django.contrib import admin

from .models import Deck, Card, Language, Topic


# admin.site.register(Deck)
class CardInline(admin.TabularInline):
    model = Card
    fields = ('front_card', 'back_card', 'image_card')


@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    """
    Class for representing the decks in the django admin panel.
    """
    list_display = ('deck_name', 'language', 'topic',
                    'status', 'creation_time')
    list_filter = ('language', 'topic',
                   'status', 'creation_time')

    fieldsets = (
        ("Назовите вашу колоду карт", {
            'fields': ('deck_name',)
        }),
        ('Выберите язык и тематику колоды', {
            'fields': ('language', 'topic')
        }),
    )

    inlines = [CardInline]


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    """
    Class for representing the cards in the django admin panel.
    """

    def deck_name(self, obj):
        return obj.deck.deck_name

    deck_name.short_description = 'Deck Name'

    def topic_name(self, obj):
        return obj.deck.topic.topic_name if obj.deck.topic else None

    topic_name.short_description = 'Topic Name'

    def language(self, obj):
        return obj.deck.language.language_name

    language.short_description = 'Language'

    list_display = ('front_card', 'back_card', 'image_card', 'deck_name', 'topic_name',
                    'repeat', 'creation_time')
    list_filter = ('deck__deck_name', 'deck__topic__topic_name', 'deck__language__language_name',
                   'repeat', 'creation_time')

    fieldsets = (
        ("Выберите к какой колоде карт добавить карточку", {
            'fields': ('deck',)
        }),
        ('Определите содержание карточки', {
            'fields': ('front_card', 'back_card', 'image_card')
        }),
    )


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
