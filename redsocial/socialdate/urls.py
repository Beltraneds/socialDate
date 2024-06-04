from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro_usuario, name='registro'),
    path('seleccion-intereses/', views.seleccion_intereses, name='seleccion_intereses'),
    path('home/', views.home_view, name='home'),  # Define la vista para 'home'
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)