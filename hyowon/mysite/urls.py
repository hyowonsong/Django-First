from django.contrib import admin
from django.urls import include, path
from mysite import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('polls/', include('polls.urls')),
    path('books/', include('books.urls')),
    path('common/', include('common.urls')),
]
