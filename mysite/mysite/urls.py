from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('agenda_personal/', include('agenda_personal.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
