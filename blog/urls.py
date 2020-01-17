
"""mysite URL COnfiguration

[...]
"""

from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('admin/', admin.site.urls)
]
