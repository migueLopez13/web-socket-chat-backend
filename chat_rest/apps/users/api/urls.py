from django.urls import path
from apps.users.api.api import user_api_view, user_detail_api_view

urlpatterns = [
    path('', user_api_view, name='users'),
    path('<int:pk>/', user_detail_api_view, name='user_detail')
]
