from django.contrib import admin
from django.urls import path, include

from upload_site import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls'), name='blog'),
    path('__debug__', include('debug_toolbar.urls')),
]
