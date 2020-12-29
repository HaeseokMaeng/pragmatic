from django.urls import path, include
from . import views

app_name = 'commentapp'

urlpatterns = [
    # path('hello/', views.Hello, name='hello'),
    # path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    #
    path('create/', views.CommentCreateView.as_view(), name='create'),
    # path('detail/<int:pk>', views.AccountDetailView.as_view(), name='detail'),
    # path('update/<int:pk>', views.AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.CommentDeleteView.as_view(), name='delete'),
]