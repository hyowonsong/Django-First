from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # 새로 추가된 부분

app_name = 'common'

urlpatterns = [
    path('', views.index, name='index'),  # index 뷰 추가
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
