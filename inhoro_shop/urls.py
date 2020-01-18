from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from inhoro_shop.core.views import IndexView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('core/', include('inhoro_shop.core.urls'))
]
