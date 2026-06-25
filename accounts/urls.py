from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # include the default auth urls
    path('', include('django.contrib.auth.urls'))
]