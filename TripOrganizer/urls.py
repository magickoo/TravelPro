
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    #auth
    path('signup', user_views.signup.as_view(), name='signup'),
    path('', auth_views.LoginView.as_view(
        template_name='user/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'),
         name='user-logout'),
    #profile
    path('profile', user_views.profile, name='user-profile'),
    path('profile/update/', user_views.profile_update, name='user-profile-update'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)