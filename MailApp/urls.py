from django.urls import path, include

from . import views

urlpatterns = [
    path('send_email/', views.send_email, name='send-email')
]
