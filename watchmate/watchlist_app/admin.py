from django.contrib import admin
from watchlist_app.models import StreamPlatform, WatchList, Reviews

admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Reviews)