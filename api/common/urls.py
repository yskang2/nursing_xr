from django.urls import path
from api.common import sample_handler

app_name = 'sample_api'

urlpatterns = [
    path('login/', sample_handler.SampleHandler.as_view(), name='sample_test'),
]