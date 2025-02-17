from django.urls import path
from . import views


app_name = 'travel'

urlpatterns = [
    path('list/', views.travel_list, name='list'),
    path('create/', views.create_destination, name='create'),
    path('detail/<int:travel_id>', views.travel_detail, name='detail'),
    path('delete/<int:travel_id>', views.travel_delete, name='delete'),
    path('update/<int:travel_id>', views.travel_update, name='update'),
]