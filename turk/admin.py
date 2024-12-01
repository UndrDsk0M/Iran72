from django.contrib import admin
from . import models

class WordTrAdmin(admin.ModelAdmin):
    list_display = ("word_pr", "word_lt", "meaning")
    search_fields = ("word_pr", "word_lt", "meaning")


admin.site.register(models.word_tr, WordTrAdmin)