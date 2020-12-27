from django.urls import path, include
from . import views

app_name = 'profileapp'

urlpatterns = [
    # path('hello/', views.Hello, name='hello'),
    # path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    # path('detail/<int:pk>', views.AccountDetailView.as_view(), name='detail'),

    path('create/', views.ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.ProfileUpdateView.as_view(), name='update'),

]
