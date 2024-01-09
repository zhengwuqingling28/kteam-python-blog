from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('contact/',views.contact),
    path('register/',views.register),
    path('login/',views.user_login),
    path('logout/',views.user_logout)
]

# Chỉ thêm định tuyến trong môi trường phát triển
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)