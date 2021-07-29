from django.contrib import admin
from .models import Question
from .models import Choice

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    # fields=['pub_date','question_text']
    fieldsets=[
        (None, {'fields':['question_text']}),
        (None, {'fields':['link']}),
        # ('Date information', {'fields':['pub_date']}),
    ]

admin.site.register(Question,QuestionAdmin)    
admin.site.register(Choice)