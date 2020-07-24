from django.contrib import admin

from .models import Submit, Picture


class PictureInline(admin.TabularInline):
    model = Picture
    extra = 0


@admin.register(Submit)
class SubmitAdmin(admin.ModelAdmin):
    inlines = [PictureInline, ]
    list_display = ('user', 'date', )
    list_filter = ('user__username', )
    date_hierarchy = 'date'
    fields = ('user', 'date')

