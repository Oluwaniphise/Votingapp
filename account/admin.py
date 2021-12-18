from django.contrib import admin
from .models import Profile, Course, Choice, Question


admin.site.register(Profile)
admin.site.register(Course)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
# Register your models here.


