from django.contrib import admin
from django.urls import path
from chat.views import send_message, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('send-message/', send_message, name='send_message'),
]
