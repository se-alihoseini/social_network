from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_account'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('profile/<int:id>', views.UserProfileView.as_view(), name='user_profile'),
    path('reset/', views.UserPasswordRestView.as_view(), name='reset_password'),
    path('reset/done/', views.UserPasswordResetDoneView.as_view(), name='reset_password_done'),
    path('confirm/<uidb64>/<token>', views.UserPaswordResetCondirmView.as_view(), name='reset_password_confirm'),
    path('confirm/comlete', views.PasswordResetCompleteView.as_view(), name='password_reset_comlete'),
    path('follow/<int:user_id>', views.UserFollowView.as_view(), name='User_Follow'),
    path('unfollow/<int:user_id>', views.UserUnFollowView.as_view(), name='User_UnFollow'),
    path('edit/', views.EditProfileViews.as_view(), name='edit_profile')
]
