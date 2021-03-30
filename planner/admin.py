from django.contrib import admin

# Register your models here.
from .models import Courses, Saved_Data, Semesters, Offered_In

admin.site.register(Courses)

admin.site.register(Saved_Data)

admin.site.register(Semesters)

admin.site.register(Offered_In)