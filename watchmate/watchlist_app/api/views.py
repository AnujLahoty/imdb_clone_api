from watchlist_app.models import WatchList, StreamPlatform, Reviews
# from rest_framework.decorators import api_view
from watchlist_app.api.serializers import (WatchListSerializer, StreamPlatformSerializer, 
                                           ReviewSerializer)
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from watchlist_app.api.permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly

class ReviewsCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Reviews.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        
        review_user = self.request.user
        review_queryset = Reviews.objects.filter(watchlist=watchlist, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("You had already reviewed the movie!")
        
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
            
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2 
            
        watchlist.number_rating += 1
        watchlist.save()    
    
        serializer.save(watchlist=watchlist, review_user=review_user)

class ReviewsList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Reviews.objects.filter(watchlist=pk)
    
    
class ReviewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


class WatchListAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, *args, **kwargs):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchDetailAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movie)
            return Response(serializer.data) 
        except WatchList.DoesNotExist: # Important part of code here
            return Response({'Error':'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StreamPlatformListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
       
class StreamPlatformDetailAV(APIView): 
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, pk):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(movie)
            return Response(serializer.data) 
        except StreamPlatform.DoesNotExist: # Important part of code here
            return Response({'Error':'Platform not found!'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        movie = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(movie, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)