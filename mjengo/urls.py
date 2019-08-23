from django.urls import path
from .views import ListCreateMaterialsView, MaterialsDetailView, LoginView, RegisterUsers, ListCreateProjectView, \
    ProjectDetailView, ListCreateRequestView, RequestDetailView
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # urls for projects
    path('projects/', ListCreateProjectView.as_view(), name="projects-list-create"),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name="projects-detail"),

    # urls for materials
    path('materials/', ListCreateMaterialsView.as_view(), name="materials-list-create"),
    path('materials/<int:pk>/', MaterialsDetailView.as_view(), name="materials-detail"),

    # urls for requests
    path('requests/', ListCreateRequestView.as_view(), name="requests-list-create"),
    path('requests/<int:pk>/', RequestDetailView.as_view(), name="requests-detail"),

    # urls for login and register
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsers.as_view(), name="auth-register"),

]
