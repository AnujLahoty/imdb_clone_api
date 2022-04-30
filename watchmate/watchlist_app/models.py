from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class StreamPlatform(models.Model):
    name = models.CharField(max_length=33)
    about = models.CharField(max_length=33)
    website = models.URLField(max_length=333)
    
    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=33)
    storlyline = models.TextField(max_length=333)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    
    def __str__(self):
        return self.title
    
class Reviews(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])    
    description = models.TextField(max_length=333, null=True, blank=True)
    watchlist=models.ForeignKey(WatchList,on_delete=models.CASCADE, related_name="reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating) + "|" + self.watchlist.title
    