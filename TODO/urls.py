from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/',include('todo_list.urls')),
    path('',include('accounts.urls')),
    path('accounts/', include('allauth.urls'))
]
