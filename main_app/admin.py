from django.contrib import admin
from .models import Plant, Quiz, QuizSubmit

# Register your models here.
admin.site.register(Plant)
admin.site.register(Quiz)
admin.site.register(QuizSubmit)