from django.urls import path
#from . import views
from .views import HomeView, PostView, AddPostView

urlpatterns = [
#   path('', views.home, name='home')
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostView.as_view(), name='post-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
] 

