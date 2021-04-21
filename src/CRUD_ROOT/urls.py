from django.contrib import admin
from django.urls import path
from App_Enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserAddShowView.as_view(), name='show_data'),
    path('show/', views.UserAddShowView.as_view(), name='show_data'),
    path('delete/<int:id>/', views.UserDeleteView.as_view(), name='delete_data'),
    path('update/<int:id>/', views.UserUpdateView.as_view(), name='update_data')
 
]
