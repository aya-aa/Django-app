from django.urls import path
from . import views
from .views import FileFieldFormView

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    #path('upload/'), upload_file, name='upload'),
    path('posts/',views.posts, name='posts'),
    path('upload/', FileFieldFormView.as_view(), name='upload_form'),
    path('upload/success/', views.upload_success, name='upload_success'),



]