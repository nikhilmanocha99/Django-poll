from django.contrib import admin
from main.models import Choice, Poll


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_recently')
    fieldsets = [('Question Name', {'fields': ['question']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]

    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['questions']
    date_hierarchy = 'pub_date'


admin.site.register(Poll, PollAdmin)