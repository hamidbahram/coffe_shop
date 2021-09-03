from django.urls import path, re_path
from app_coffeshop import views


urlpatterns = [
    path(r'', views.PostListAPIView.as_view()),
]