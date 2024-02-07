from django.urls import path

from .views import SignUpView, CreateWorkspaceView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('profiles/create/', CreateWorkspaceView.as_view())
]