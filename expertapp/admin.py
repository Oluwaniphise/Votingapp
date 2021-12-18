from django.contrib import admin
from .models import Choice, Question

# # Register your models here.
# admin.site.register(PoliticalPost)
# admin.site.register(politicians)



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]