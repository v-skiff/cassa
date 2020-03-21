from django.urls import path, include
from .views import IndexView

urlpatterns = [
    path('/', include(main.urls, namespace='')),
]
