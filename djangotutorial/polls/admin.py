from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    # Another possibility is StackedInline
    # class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # Define the order of fields in admin record view
    # fields = ["pub_date", "question_text"]

    # Define fieldsets to group fields in admin record view
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]

    # To display individual fields instead of str() of object
    list_display = ["question_text", "pub_date", "was_published_recently"]

    # Add filter sidebar by pub_date
    list_filter = ["pub_date"]

    # Add search box for question_text
    search_fields = ["question_text"]

    # Inline view of choices in question edit view
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
