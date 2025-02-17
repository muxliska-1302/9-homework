from django.urls import path
from . import views


app_name = 'sports'

urlpatterns = [
    path('list/', views.event_list, name='list'),
    path('create/', views.create_event, name='create'),
    path('detail/<int:event_id>', views.event_detail, name='detail'),
    path('delete/<int:event_id>', views.event_delete, name='delete'),
    path('update/<int:event_id>', views.event_update, name='update'),
]