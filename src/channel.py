import os
import json
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id

        service = Channel.get_service()
        parts = 'snippet,statistics'
        result = service.channels().list(id=channel_id, part=parts).execute()
        channel = result['items'][0]['snippet']
        statistics = result['items'][0]['statistics']

        self.id = channel_id
        self.title = channel['title']
        self.description = channel['description']
        self.url = f"https://www.youtube.com/channel/{self._channel_id}"
        self.subscriber_count = statistics['subscriberCount']
        self.video_count = statistics['videoCount']
        self.view_count = statistics['viewCount']

    def __str__(self):
        return f"Канал {self.title} - {self.url}"

    def __add__(self, other) -> int:
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other) -> int:
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __sub__(self, other) -> int:
        return int(other.subscriber_count) - int(self.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __eq__(self, other):
        return int(self.subscriber_count) == int(other.subscriber_count)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
        print(channel)

    @property
    def channel_id(self):
        return self._channel_id

    @classmethod
    def get_service(cls):
        """
        Возвращает объект для работы с YouTube API
        """
        return youtube

    def to_json(self, filename):
        """
        Сохраняет в файл значения атрибутов экземпляра Channel
        """
        data = {
            'channel_id': self._channel_id,
            'title': self.title,
            'about': self.description,
            'url': self.url,
            'subscribers_counter': self.subscriber_count,
            'videos_total': self.video_count,
            'views_total': self.view_count
        }
        with open(filename, 'w') as f:
            json.dump(data, f)
