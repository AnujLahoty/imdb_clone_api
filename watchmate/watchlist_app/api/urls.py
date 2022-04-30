from django.urls import path
from watchlist_app.api.views import (WatchListAV, WatchDetailAV, 
                                     StreamPlatformListAV, StreamPlatformDetailAV, 
                                     ReviewsList, ReviewsDetail, ReviewsCreate)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('stream/<int:pk>/reviews/', ReviewsList.as_view(), name='review-list'),
    path('stream/<int:pk>/review-create/', ReviewsCreate.as_view(), name='review-create'),
    path('stream/reviews/<int:pk>/', ReviewsDetail.as_view(), name='review-detail'),
]
