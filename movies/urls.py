from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('list/', views.movie_list, name='list'),
    path('create/', views.create_movie, name='create'),
    path('detail/<int:movie_id>', views.movie_detail, name='detail'),
    path('delete/<int:movie_id>', views.movie_delete, name='delete'),
    path('update/<int:movie_id>', views.movie_update, name='update'),
]