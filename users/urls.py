from django.urls import path
from.views import userregister

urlpatterns = [
    path('register/',userregister.as_view(),name='register'),

]