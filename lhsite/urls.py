from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about-us/', views.about_us, name='about-us'),
    path('events/', include('events.urls')),
    path('sermons/', views.sermons, name='sermons'),
    path('contact-us/', views.contact_us, name='contact-us'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
