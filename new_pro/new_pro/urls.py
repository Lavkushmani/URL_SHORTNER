
from django.contrib import admin
from django.urls import path, include

from shorten.views import index, create, goto, update, delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index, name="index"),
    path('', create, name="create"),
    path('<str:shortcode>/', goto, name="redirect"),
    path('edit/<int:pk>/', update, name="update"),
    path('delete/<int:pk>/', delete, name="delete"),
    path('accounts/', include('allauth.urls')),
]
