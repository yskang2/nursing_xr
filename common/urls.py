from django.urls import path
from common.views import base_views

app_name = "common"

urlpatterns = [
    # path('', base_views.index, name=''),
    # path("", base_views.Home.as_view(), name="home"),
    path("", base_views.MainPage.as_view(), name="main"),
]
