from __future__ import unicode_literals
from django.shortcuts import render
from api.views import get_search_video_list, get_related_video, get_video_by_token, get_video_info
from api.views import VideoClass
from django.http import HttpResponseNotFound


# Create your views here.

def home_view(request):

    return render(request, 'index.html')


# search_video view for getting all video with matching channel ID
def search_video(request):
    query = request.POST.get("search_video")

    try:
        api_response = get_search_video_list(query)
        return render(request, 'index.html',
                      {'video_list': get_list_of_video(api_response), 'nextPageToken': api_response['nextPageToken'],
                       'query': query})

    except:

        return HttpResponseNotFound("<h4>Invalid Query, Please Enter channel ID!!!</h4>")


# watch_video function for rendering watch.html page with data
def watch_video(request, vid_id):
    video_info = get_video_info(vid_id)
    filtered_video = get_list_of_video(get_related_video(vid_id))

    context = {'vid_id': vid_id, 'video_list': filtered_video, 'video_info': video_info}
    return render(request, 'watch.html', context)


# get_list_of_video for converting json to list of VideoClass objects
def get_list_of_video(search_response):
    video_list = []

    for video in search_response.get("items", []):
        if video["id"]["kind"] == "youtube#video":
            video_obj = VideoClass()
            video_obj.id = video["id"]["videoId"]
            video_obj.title = video["snippet"]["title"]
            video_obj.thumbnail = video["snippet"]["thumbnails"]["medium"]["url"]
            video_obj.description = video["snippet"]["description"]
            video_obj.channelTitle = video["snippet"]["channelTitle"]
            video_obj.channelId = video["snippet"]["channelId"]
            video_obj.publishedAt = video["snippet"]["publishedAt"]
            video_list.append(video_obj)

    return video_list


# next_token function fpor getting next 50 videos
def next_token(request, next_page_token):
    page_token = next_page_token[0:6]
    query = next_page_token[7:]
    api_response = get_video_by_token(page_token, query)
    return render(request, 'index.html', {'video_list': get_list_of_video(api_response), 'nextPageToken': None})
