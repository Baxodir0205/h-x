from django.contrib import admin

from .models import *

class IncorrectInline(admin.StackedInline):
 model = Incorrect
 extra =1


@admin.register(Correct)
class CorrectAdmin(admin.ModelAdmin):
    list_display = ('word',)
    inlines = (IncorrectInline,)


@admin.register(Incorrect)
class IncorrectAdmin(admin.ModelAdmin):
    list_display = ('word','correct')