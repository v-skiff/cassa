from django.urls import path
from django.views.decorators.cache import never_cache
from django.contrib.staticfiles.views import serve
from django.conf.urls.static import static
from django.conf import settings
from .views import (IndexView, MemberList, MemberDelete, MemberUpdate, MemberCreate, LoginView, LogoutView,
                    PaymentList, PaymentDelete, PaymentUpdate, PaymentCreate, MainReport)

urlpatterns = [
    path('report/main/', MainReport.as_view(), name="main_report"),
    path('payment/create/', PaymentCreate.as_view(), name="payment_create"),
    path('payment/update/<int:pk>/', PaymentUpdate.as_view(), name="payment_update"),
    path('payment/delete/<int:pk>/', PaymentDelete.as_view(), name="payment_delete"),
    path('payment/list/', PaymentList.as_view(), name="payment_list"),
    path('member/create/', MemberCreate.as_view(), name="member_create"),
    path('member/update/<int:pk>/', MemberUpdate.as_view(), name="member_update"),
    path('member/delete/<int:pk>/', MemberDelete.as_view(), name="member_delete"),
    path('member/list/', MemberList.as_view(), name="member_list"),
    path('accounts/logout/', LogoutView.as_view(), name="logout"),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('', IndexView.as_view(), name="index"),
]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)