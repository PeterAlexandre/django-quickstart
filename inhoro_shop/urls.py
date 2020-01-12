from django.contrib import admin
from django.urls import path, include

from inhoro_shop.core.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('core/', include('inhoro_shop.core.urls'))
]
