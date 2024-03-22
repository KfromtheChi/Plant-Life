from django.contrib import admin
from .models import Plant, Plant_Care, Quiz, QuizSubmit

# Register your models here.
admin.site.register(Plant)
admin.site.register(Plant_Care)
admin.site.register(Quiz)
admin.site.register(QuizSubmit)