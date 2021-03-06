from django.urls import path
from watchlist_app.api.views import (WatchListAV, WatchDetailAV, 
                                     StreamPlatformListAV, StreamPlatformDetailAV, 
                                     ReviewsList, ReviewsDetail, ReviewsCreate, UserReview,
                                     WatchListGV)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('list2/', WatchListGV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    
    path('stream/', StreamPlatformListAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    
    path('<int:pk>/reviews/', ReviewsList.as_view(), name='review-list'),
    path('<int:pk>/review-create/', ReviewsCreate.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewsDetail.as_view(), name='review-detail'),
    path('reviews/', UserReview.as_view(), name='user-review-detail'),
]
