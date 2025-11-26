from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('octofit_app.urls')),
    path('api/', include('octofit_app.urls')),
]
