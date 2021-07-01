"""A video playlist class."""

from typing import Sequence

class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_title: str):
        self._pl_title = playlist_title
        self._pl_videos = []

    @property
    def pl_title(self) -> str:
        return self._pl_title

    @property
    def pl_videos(self) -> Sequence[str]:
        return self._pl_videos

    def addVideo(self,video_id):
        self._pl_videos.append(video_id)

    def removeVideo(self, video_id):
        self._pl_videos.remove(video_id)

    def checkVideo(self, video_id):
        if len(self._pl_videos) == 0:
            return False
        for id in self._pl_videos:
            if id == video_id:
                return True
        return False

    def clearPlaylist(self):
        self._pl_videos = []