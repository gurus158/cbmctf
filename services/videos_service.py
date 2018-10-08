from modals import videos
from dao import videos_dao

def create_video(video_details):
    if video_details is not None:
        video = videos.Video
        video.url = video_details['url']
        video.name = video_details['name']
        video.description = video_details['description']
        return video
    return None

def isempty(any_structure):
    if any_structure:
        return False
    else:
        return True

def get_video_details(video_name):
    if video_name is not  None:
        r=videos_dao.get_video_details(video_name)
        return r

def get_video_list():
    return videos_dao.get_video_list()
