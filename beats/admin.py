from django.contrib import admin
from .models import Beat, Genre, Review

# Register your models here.


class BeatAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'genre',
        'price',
        'file',
        'image',
    )

    ordering = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'beat',
        'comment',
        'user',
    )


admin.site.register(Review, ReviewAdmin)
admin.site.register(Beat, BeatAdmin)
admin.site.register(Genre, GenreAdmin)
