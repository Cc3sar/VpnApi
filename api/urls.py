from django.urls import path, include
from .viewsets import SayHelloViewSet

urlpatterns = [
    path(r'say_hello/', SayHelloViewSet.as_view({'get': 'hi'})),
]
