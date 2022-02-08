from django.urls import path
from . import views

# URLConf
urlpatterns = [
        path('helloClassBased/', views.HelloView.as_view())
]
