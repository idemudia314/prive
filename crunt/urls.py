
from django.urls import path
from .views import CruntCreateView, CruntListView, CruntDetailView, CruntUpdateView, CruntDeleteView

urlpatterns = [
    path("", CruntListView.as_view(), name ='home'),
    path('post/<int:pk>/', CruntDetailView.as_view(), name = 'post_detail'),
    path('post/new/', CruntCreateView.as_view(), name ='post_new'),
    path('post/<int:pk>/edit/', CruntUpdateView.as_view(), name ='post_edit'),
    path('post/<int:pk>/delete/', CruntDeleteView.as_view(), name ='post_delete')
    
]
