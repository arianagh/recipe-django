from django.contrib import admin

from .models import User, Tag, Recipe, Ingredient

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(Ingredient)
