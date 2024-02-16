from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('top/', views.top_people, name="top"),
    path('profile/<int:id>', views.profile, name="profile"),
    path('jozve/', views.jozve, name="jozve"),
    path('login/', views.mylogin, name="login"),
    path('logout', views.my_logout, name="logout"),
    # path('login/code<str:pw>/', views.login_with_qrcode),
    path('no-register', views.no_register, name="no-register"),
    path('top-cs', views.top_cs, name="top-cs"),
] 