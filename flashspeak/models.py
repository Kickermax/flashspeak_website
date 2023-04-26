from django.db import models
from django.urls import reverse


class Language(models.Model):
    """
    Model representing a single language.
    """
    language_id = models.AutoField(primary_key=True)
    language_name = models.CharField(max_length=255)
    language_image = models.CharField(max_length=255, null=True)

    def __str__(self):
        """
        String for representing the language name.
        """
        return self.language_name


class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    topic_name = models.CharField(max_length=255)

    def __str__(self):
        return self.topic_name


class Deck(models.Model):
    """
    Model representing a deck of cards (not a single card)
    """
    deck_id = models.AutoField(primary_key=True)
    deck_name = models.CharField(max_length=255)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, models.SET_NULL, null=True)
    STATUS_CHOICES = [
        (0, 'Not learned'),
        (1, 'Learned'),
    ]
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String for representing the deck name.
        """
        return self.deck_name

    def get_absolute_url(self):
        """
        Generate the URL for the Deck of Cards detail view.

        Returns:
            str: Absolute URL of the Deck of Cards instance.
        """
        return reverse('view_name', kwargs={'deck_id': self.deck_id})
        # todo шаблон написать потом


class Card(models.Model):
    """
    Model representing a single card
    """
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card_id = models.AutoField(primary_key=True)
    front_card = models.CharField(max_length=255)
    back_card = models.CharField(max_length=255)
    image_card = models.CharField(max_length=255, null=True, blank=True)
    REPEAT_CHOICES = [
        (0, 'Again (< 1 day)'),
        (1, 'One day later'),
        (2, 'Four days later'),
        (3, 'Twenty-one days later')
    ]
    repeat = models.PositiveSmallIntegerField(choices=REPEAT_CHOICES, default=0)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String for representing the card content.
        """
        return f"{self.front_card} - {self.back_card}"

    def get_absolute_url(self):
        """
        Generate the URL for the Card detail view.

        Returns:
            str: Absolute URL of the Card instance.
        """
        return reverse('view_name', kwargs={'card_id': self.card_id})
        # todo шаблон написать потом
