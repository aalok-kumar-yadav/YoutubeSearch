# importing required packages

from django.conf.urls import url
from django.contrib import admin
from index.views import home_view, watch_video, next_token, search_video

# URL Patterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search$', search_video, name='search_video'),
    url(r'^watch_id=(?P<vid_id>[-\w\+%_& ]+)$', watch_video, name='watch_video'),
    url(r'^token=(?P<next_page_token>[-\w\+%_& ]+)$', next_token, name='next_token'),
    url(r'^$', home_view, name='home_view'),

]
