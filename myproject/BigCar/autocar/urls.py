from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.home, name='home'),
    path('cars/', views.car_list, name='cars'),
    path('image/', views.image_view, name='image-view'),

]

# This is only needed when you are in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)