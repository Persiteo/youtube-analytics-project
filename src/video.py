import os
from googleapiclient.discovery import build


class Video:
    """
    to be continued...
    """
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        parts = 'snippet,statistics'
        result = self.youtube.videos().list(id=video_id, part=parts).execute()
        statistics = result['items'][0]['statistics']

        self.video_id = video_id
        self.id = video_id
        self.title = result['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/channel/{self.video_id}"
        self.views_count = statistics['viewCount']
        self.likes_count = statistics['likeCount']

    def __str__(self):
        return self.title


class PLVideo (Video):
    """
        to be continued, maybe...
        """
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str_(self):
        return self.title
