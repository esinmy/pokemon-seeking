from django.db import models


class Pokemon(models.Model):
    title = models.CharField("имя", max_length=200)
    title_en = models.CharField("имя (англ.)", max_length=200, blank=True)
    title_jp = models.CharField("имя (яп.)", max_length=200, blank=True)
    description = models.TextField("описание", blank=True)
    img = models.ImageField("картинка", upload_to='pokemon_img', null=True, blank=True)
    previous_evolution = models.ForeignKey("Pokemon", null=True, blank=True,
                                           verbose_name='предок',
                                           on_delete=models.SET_NULL,
                                           related_name="next_evolutions")

    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='покемон', on_delete=models.CASCADE, related_name="entities")
    lat = models.FloatField("широта")
    lon = models.FloatField("долгота")
    appeared_at = models.DateTimeField("время появления", null=True, blank=True)
    disappeared_at = models.DateTimeField("время исчезновения", null=True, blank=True)
    level = models.IntegerField("уровень", null=True, blank=True)
    health = models.IntegerField("здоровье", null=True, blank=True)
    strength = models.IntegerField("атака", null=True, blank=True)
    defence = models.IntegerField("защита", null=True, blank=True)
    stamina = models.IntegerField("выносливость", null=True, blank=True)

    def __str__(self):
        return f"{self.pokemon.title} (когда исчезнет: {self.disappeared_at})"
