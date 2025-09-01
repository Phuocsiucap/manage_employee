from django.urls import path
from . import views

urlpatterns = [
    path("", views.createWork_scheduleView.as_view(), name="create_work_schedule"),
]
