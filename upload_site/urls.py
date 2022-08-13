from django.contrib import admin
from django.urls import path, include

from upload_site import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('__debug__', include('debug_toolbar.urls')),
]
