from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from django.urls import path
from planner import views
# from django.urls import path

from django.contrib import admin
from django.urls import path

from planner import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('planner/', include('planner.urls')), # new
    path('planner/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('', FYP-Interface.public.index.html),
    path('admin/', admin.site.urls),
    path('courses', views.course_list),
    path('prerequisite', views.prerequisite_list),
    path('semesters', views.semester_list),
    path('offered_in', views.offered_in_list),
    path('courses/offered_in/<slug:cid>', views.offered_in_course),
]
