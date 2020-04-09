import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemon_entities = PokemonEntity.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon_entity.pokemon.title, request.build_absolute_uri(pokemon_entity.pokemon.img.url))

    pokemons_on_page = []
    for pokemon in Pokemon.objects.all():
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.img.url,
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)

    pokemon_info = {"title_ru": pokemon.title,
                    "title_en": pokemon.title_en,
                    "title_jp": pokemon.title_jp,
                    "description": pokemon.description,
                    "img_url": request.build_absolute_uri(pokemon.img.url),
                    }
    if pokemon.previous_evolution:
        pokemon_info["previous_evolution"] = {"pokemon_id": pokemon.previous_evolution.id,
                                              "title_ru": pokemon.previous_evolution.title,
                                              "img_url": request.build_absolute_uri(pokemon.previous_evolution.img.url),
                                              }

    next_evolution = pokemon.next_evolutions.first()
    if next_evolution:
        pokemon_info["next_evolution"] = {"pokemon_id": next_evolution.id,
                                          "title_ru": next_evolution.title,
                                          "img_url": request.build_absolute_uri(next_evolution.img.url),
                                          }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for entity in pokemon.entities.all():
        add_pokemon(
            folium_map, entity.lat, entity.lon,
            entity.pokemon.title, pokemon_info["img_url"])


    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon_info})
