from django.urls import path, include
from . import views

app_name = 'subscriptionapp'

urlpatterns = [
    # path('list/', views.ProjectListView.as_view(), name='list'),
    # path('create/', views.ProjectCreateView.as_view(), name='create'),
    # path('detail/<int:pk>', views.ProjectDetailView.as_view(), name='detail'),
    path('subscribe/', views.SubscriptionRedirectView.as_view(), name='subscribe'),
]
