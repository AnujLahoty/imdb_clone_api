from django.urls import path
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformListAV, StreamPlatformDetailAV, ReviewsList, ReviewsDetail

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('reviews/', ReviewsList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewsDetail.as_view(), name='review-detail'),
]
