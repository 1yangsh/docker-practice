from django.contrib import admin
from django.urls import path, include


# from rest_framework import routers
# from blog import rest_views

# router = routers.DefaultRouter()
# router.register(r'users', rest_views.UserViewSet)

urlpatterns = [


    # http://127.0.01:8000/ -> home page
    path('admin/', admin.site.urls),
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),


]
