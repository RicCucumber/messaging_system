from django.urls import path, include
from .views import MessageViewSet


create_message = MessageViewSet.as_view({'post': 'create'})
list_messages = MessageViewSet.as_view({'get': 'list'})
detail_message = MessageViewSet.as_view({'get':'details', 'delete': 'destroy'})

urlpatterns = [
    path('new/', create_message),
    path('', list_messages),
    path('<int:pk>/', detail_message)
]
