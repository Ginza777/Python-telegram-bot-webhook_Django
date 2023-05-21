from django.db import models


class Language(models.TextChoices):
    UZBEK = "uz", "Uzbek",
    RUSSIAN = "ru", "Russian",
    ENGLISH = "en", "English",


class TelegramProfile(models.Model):
    telegram_id = models.PositiveBigIntegerField(unique=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, choices=Language.choices, default=Language.UZBEK,null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username} {self.telegram_id}"



class Country(models.Model):
    name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
class Region(models.Model):
    name=models.CharField(max_length=200,null=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.name}        {self.country.name}"
