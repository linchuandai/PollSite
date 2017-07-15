from django.contrib import admin
from .models import Question, Choice

#Two types: StackedInLine and TabularInLine
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'],
        'classes' : ['collapse']}),
        ]
    inlines = [ChoiceInLine]

    list_display = ('question_text', 'was_published_recently')

    list_filter = ['pub_date']

    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)