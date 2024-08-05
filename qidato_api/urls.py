from django.contrib import admin
from django.urls import path, include
from accounts.views import CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/logout/', CustomLogoutView.as_view(), name='custom_logout'),
    path('api/', include('accounts.urls')),
    path('api/', include('attendance.urls')),
    path('api/', include('grading.urls')),
]
