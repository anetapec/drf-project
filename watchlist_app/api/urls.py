from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import MovieDetailAV, WatchList

urlpatterns = [
    path('list/',WatchList.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailAV.as_view(), name='movie-datail')
]
