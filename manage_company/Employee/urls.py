from django.urls import path
from . import views

urlpatterns = [
    path("create", views.createEmployeeView.as_view(), name="create_employee"),
    path("", views.getEmployeeView.as_view(), name="list_employee"),
]