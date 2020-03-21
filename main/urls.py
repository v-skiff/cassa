from django.urls import path
from django.views.decorators.cache import never_cache
from django.contrib.staticfiles.views import serve
from django.conf.urls.static import static
from django.conf import settings
from .views import IndexView, LoginView, LogoutView

urlpatterns = [
    path('accounts/logout', LogoutView.as_view(), name="logout"),
    path('accounts/login', LoginView.as_view(), name="login"),
    path('', IndexView.as_view(), name="index"),
]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)