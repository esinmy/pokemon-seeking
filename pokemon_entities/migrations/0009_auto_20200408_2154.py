# Generated by Django 2.2.3 on 2020-04-08 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_auto_20200408_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='Здесь будет описание покемона', verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='pokemon_img', verbose_name='картинка'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.Pokemon', verbose_name='предок'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=200, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(default='tba', max_length=200, verbose_name='имя (англ.)'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(default='tba', max_length=200, verbose_name='имя (яп.)'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время появления'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(blank=True, null=True, verbose_name='защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время исчезновения'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, null=True, verbose_name='здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(verbose_name='широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, null=True, verbose_name='уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lon',
            field=models.FloatField(verbose_name='долгота'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='pokemon_entities.Pokemon', verbose_name='покемон'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(blank=True, null=True, verbose_name='выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(blank=True, null=True, verbose_name='атака'),
        ),
    ]