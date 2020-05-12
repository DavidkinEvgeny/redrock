from django.contrib import admin

from .models import Party, Album


class AlbumInLine(admin.TabularInline):
    model = Album
    extra = 3


class PartyAdmin(admin.ModelAdmin):
    fields = ["title", "event_date", "preview", "text_before", "text_after"]
    inlines = [AlbumInLine]


admin.site.register(Party, PartyAdmin)

