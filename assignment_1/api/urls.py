from django.urls import path
from assignment_1.api.views import (
    registration_view,
)

app_name = "assignment"

urlpatterns = [
    path('register', registration_view, name="register")
]