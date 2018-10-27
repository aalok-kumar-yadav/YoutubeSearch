from googleapiclient.discovery import build

# Google developer key for fetching data from youtube server
DEVELOPER_KEY = "AIzaSyDy7uIm3_OBOibaOpe34voXfvMeQfJuSpw"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)


# VideoClass  With Attributes
class VideoClass:
    id = ''
    title = ''
    thumbnail = ''
    description = ''
    channelTitle = ''
    channelId = ''
    publishedAt = ''


# get_video_list function for getting all videos of search_query
def get_search_video_list(search_query):
    search_response = youtube.search().list(channelId=search_query,
                                            part="id,snippet",
                                            maxResults=50
                                            ).execute()

    return search_response


# get_video_by_token for getting next 50 videos of same query
def get_video_by_token(next_page_token, query):
    search_response = youtube.search().list(
        channelId=query,
        part="id,snippet",
        maxResults=50,
        pageToken=next_page_token
    ).execute()

    return search_response


# get_related_video for getting related video of given video id
def get_related_video(vid_id):
    search_response = youtube.search().list(
        part='snippet',
        type='video',
        relatedToVideoId=vid_id,
        key=DEVELOPER_KEY,
        maxResults=5
    ).execute()

    return search_response


# get_video_info for getting view count, like count, title
def get_video_info(vid_id):
    search_response = youtube.videos().list(
        part='snippet, statistics',
        id=vid_id
    ).execute()

    context = {'viewCount': search_response['items'][0]['statistics']['viewCount'],
               'likeCount': search_response['items'][0]['statistics']['likeCount'],
               'title': search_response['items'][0]['snippet']['title'],
               'description': search_response['items'][0]['snippet']['description'],
               'channelId': search_response['items'][0]['snippet']['channelId']
               }

    return context
