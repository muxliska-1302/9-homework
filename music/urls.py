from django.urls import path
from . import views


app_name = 'music'

urlpatterns = [
    path('list/', views.music_list, name='list'),
    path('create/', views.create_album, name='create'),
    path('detail/<int:music_id>', views.album_detail, name='detail'),
    path('delete/<int:music_id>', views.album_delete, name='delete'),
    path('update/<int:music_id>', views.album_update, name='update'),
]