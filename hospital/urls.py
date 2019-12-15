from django.urls import path
from hospital import views

app_name = 'hospital'

urlpatterns = [
    path('login', views.LoginPage , name = 'login'),
    path('submitform',views.submit_details, name = 'submitform'),
    path('logout', views.LogoutPage, name = 'logout')
]
