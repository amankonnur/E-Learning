from django.urls import path
from users import views


urlpatterns = [
    path('home/',views.homeview,name='course_home'),
    path('login/',views.LoginView.as_view(),name='login')
]