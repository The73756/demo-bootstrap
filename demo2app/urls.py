from django.contrib.auth.views import LogoutView
from django.urls import path

from demo2app.views import *

urlpatterns = [
    path('', RequestListView.as_view(), name='home'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('registration', CustomRegistrationView.as_view(), name='registration'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('create-request', CreateRequestView.as_view(), name='create-request'),
    path('site-admin', AdminRequestsView.as_view(), name='admin-index'),
    path('site-admin/edit/<int:pk>', EditRequestView.as_view(), name='edit-request')
]
