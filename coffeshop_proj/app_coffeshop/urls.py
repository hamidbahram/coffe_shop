from django.urls import path, re_path
from app_coffeshop import views


urlpatterns = [
    path(r'product/', views.ProductListAPIView.as_view()),
    path(r'optiont/', views.OptionListAPIView.as_view()),
    path(r'order/', views.OrderListAPIView.as_view()),
    path(r'optionvalue/', views.OrderListAPIView.as_view()),
    path(r'userlist/', views.UserListAPIView.as_view()),
    path(r'createuser/', views.UserCreate.as_view()),
]
