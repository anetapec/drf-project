from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import  (WatchListAV, WatchDetailAV, StreamPlatformAV, 
                                      StreamPlatformDetailAV, ReviewList, ReviewDetail)


urlpatterns = [
    path('list/',WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-datail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    # path('stream/<int:pk>/review', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    # path('stream/review/<int:pk>', ReviewDatail.as_view(), name='review-detail'),
    
    path('review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]
