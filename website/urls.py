from django.urls import path
from . import views
from .views import FileFieldFormView

urlpatterns = [
    path('', views.home, name='home'),
    path('adminpage/',views.admin_page, name='admin_page'),
    path('adminpage/management',views.admin_manage, name='admin_manage'),

    path('adminpage/management/add_post/', views.add_post, name='add_post'),
    path('adminpage/management/edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('adminpage/management/delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    #path('upload/'), upload_file, name='upload'),
    path('posts/',views.posts, name='posts'),
    path('upload/', FileFieldFormView.as_view(), name='upload_form'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('save_history/', views.save_history_view, name='save_history'),
    path('view_history/<int:position_id>/', views.view_history, name='view_history'),
    path('view_all_history/', views.view_all_history, name='view_all_history'),
    path('view_all_history/<int:position_id>/', views.view_all_history, name='view_all_history_filtered'),




]

