from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from accounts import views as account_views
from typings import views as typing_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication
    path('api/register/', account_views.UserRegisterView.as_view(), name='register'),
    path('api/login/', account_views.UserLoginView.as_view(), name='login'),
    path('api/logout/', account_views.UserLogoutView.as_view(), name='logout'),
    path('api/user/', account_views.UserDetailView.as_view(), name='user-detail'),
    
    # Typing app
    path('api/passages/', typing_views.TextPassageList.as_view(), name='passage-list'),
    path('api/sessions/', typing_views.TypingSessionCreate.as_view(), name='session-create'),
    path('api/progress/', typing_views.UserProgressView.as_view(), name='user-progress'),
]