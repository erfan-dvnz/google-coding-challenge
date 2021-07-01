"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playing_status = ''
        self._pause = 'stopped'
        self._playlists = {}

    def getVideoInfo(self, video_id):
        title = self._video_library.get_video(video_id)._title
        id = self._video_library.get_video(video_id)._video_id
        tags = self._video_library.get_video(video_id)._tags
        str_tags = ''
        tags_size = 0
        for tag in tags:
            if tags_size > 0:
                str_tags += ' {}'.format(tag)
                tags_size += 1
            else:
                str_tags += '{}'.format(tag)
                tags_size += 1

        status = '{} ({}) [{}]'.format(
            title,
            id,
            str_tags
        )
        return status


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")


    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")

        ### Getting all videos
        list_videos = self._video_library.get_all_videos()
        lines = []

        ### Getting info in videos
        for video in list_videos:
            title = video._title
            id = video._video_id
            tags = video._tags
            str_tags = ''
            tags_size = 0
            for tag in tags:
                if tags_size > 0:
                    str_tags += ' {}'.format(tag)
                    tags_size += 1
                else:
                    str_tags += '{}'.format(tag)
                    tags_size += 1

            ### Saving each line containing video info
            line = '{} ({}) [{}]'.format(
                title,
                id,
                str_tags
            )
            lines.append(line)

        ### Sorting the lines
        lines.sort()

        ### Printing each line containing video info
        for line in lines:
            print('   {}'.format(line))


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        vid = self._video_library.get_video(video_id)

        ### If video does not exist...
        if (vid == None): print('Cannot play video: Video does not exist')

        ### If video does exist...
        else:
            ### Check another video is playing
            if self._playing_status != '':
                print('Stopping video: {}'.format(
                    self._video_library.get_video(self._playing_status)._title
                ))
            print('Playing video: {}'.format(vid._title))
            self._playing_status = video_id
            self._pause = 'playing'
        

    def stop_video(self):
        """Stops the current video."""

        ### If nothing is playing
        if self._playing_status == '':
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: {}".format(
                self._video_library.get_video(self._playing_status)._title
            ))
            self._playing_status = ''


    def play_random_video(self):
        """Plays a random video from the video library."""

        list_videos = self._video_library.get_all_videos()
        if len(list_videos) == 0:
            print('No videos available')
        else:
            choice = random.choice(list_videos)
            self.play_video(choice._video_id)


    def pause_video(self):
        """Pauses the current video."""

        if self._playing_status == '':
            print('Cannot pause video: No video is currently playing')
        else:
            if self._pause == 'playing':
                print('Pausing video: {}'.format(self._video_library.get_video(self._playing_status)._title))
                self._pause = 'paused'
            elif self._pause == 'paused':
                print('Video already paused: {}'.format(self._video_library.get_video(self._playing_status)._title))


    def continue_video(self):
        """Resumes playing the current video."""

        if self._playing_status == '':
            print('Cannot continue video: No video is currently playing')
        else:
            if self._pause == 'playing':
                print('Cannot continue video: Video is not paused')
            elif self._pause == 'paused':
                print('Continuing video: {}'.format(self._video_library.get_video(self._playing_status)._title))


    def show_playing(self):
        """Displays video currently playing."""

        if self._playing_status == '':
            print('No video is currently playing')
        else:
            video = self._video_library.get_video(self._playing_status)
            name = video._title
            id = video.video_id
            tags = video._tags
            str_tags = ''
            tags_size = 0
            for tag in tags:
                if tags_size > 0:
                    str_tags += ' {}'.format(tag)
                    tags_size += 1
                else:
                    str_tags += '{}'.format(tag)
                    tags_size += 1

            pause = ''
            if self._pause == 'paused':
                pause = ' - PAUSED'
            status = 'Currently playing: {} ({}) [{}]{}'.format(
                name,
                id,
                str_tags,
                pause
            )

            print(status)


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        name = playlist_name.lower()
        if name in self._playlists:
            print('Cannot create playlist: A playlist with the same name already exists')
        else:
            self._playlists[name] = Playlist(playlist_name)
            print('Successfully created new playlist: {}'.format(self._playlists[name]._pl_title))


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        name = playlist_name.lower()
        if name not in self._playlists:
            print('Cannot add video to {}: Playlist does not exist'.format(playlist_name))
        else:
            if self._video_library.get_video(video_id) == None:
                print('Cannot add video to {}: Video does not exist'.format(playlist_name))
                #print('Cannot add video to playlist: Video does not exist')
            else:
                if self._playlists[name].checkVideo(video_id):
                    print('Cannot add video to {}: Video already added'.format(playlist_name))
                else:
                    self._playlists[name].addVideo(video_id)
                    print('Added video to {}: {}'.format(playlist_name, self._video_library.get_video(video_id)._title))


    def show_all_playlists(self):
        """Display all playlists."""

        if len(self._playlists) == 0:
            print('No playlists exist yet')
        else:
            print('Showing all playlists:')
            pls = []
            for pl in self._playlists:
                pls.append(self._playlists[pl]._pl_title)
            pls.sort()
            for i in pls:
                print(' {}'.format(i))


    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        name = playlist_name.lower()
        if name not in self._playlists:
            print('Cannot show playlist {}: Playlist does not exist'.format(playlist_name))
        else:
            print('Showing playlist: {}'.format(playlist_name))
            videos = self._playlists[name]._pl_videos
            if len(videos) == 0:
                print(' No videos here yet')
            else:
                for vid in videos:
                    print(' {}'.format(self.getVideoInfo(vid)))


    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """

        name = playlist_name.lower()
        if name not in self._playlists:
            print('Cannot remove video from {}: Playlist does not exist'.format(playlist_name))
        else:
            if self._video_library.get_video(video_id) == None:
                print('Cannot remove video from {}: Video does not exist'.format(playlist_name))
            else:
                if self._playlists[name].checkVideo(video_id) == False:
                    print('Cannot remove video from {}: Video is not in playlist'.format(playlist_name))
                else:
                    self._playlists[name].removeVideo(video_id)
                    video = self._video_library.get_video(video_id)
                    print('Removed video from {}: {}'.format(playlist_name, self._video_library.get_video(video_id)._title))


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        name = playlist_name.lower()
        if name not in self._playlists:
            print('Cannot clear playlist {}: Playlist does not exist'.format(playlist_name))
        else:
            self._playlists[name].clearPlaylist()
            print('Successfully removed all videos from {}'.format(playlist_name))


    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        name = playlist_name.lower()
        if name not in self._playlists:
            print('Cannot delete playlist {}: Playlist does not exist'.format(playlist_name))
        else:
            self._playlists.pop(playlist_name)
            print('Deleted playlist: {}'.format(playlist_name))


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """

        ### Getting all videos
        list_videos = self._video_library.get_all_videos()
        lines = []

        ### Getting info in videos
        for video in list_videos:
            title = video._title
            id = video._video_id
            tags = video._tags
            str_tags = ''
            tags_size = 0
            for tag in tags:
                if tags_size > 0:
                    str_tags += ' {}'.format(tag)
                    tags_size += 1
                else:
                    str_tags += '{}'.format(tag)
                    tags_size += 1

            ### Saving each line containing video info
            line = '{} ({}) [{}]'.format(
                title,
                id,
                str_tags
            )
            lines.append(line)

        ### Sorting the lines
        lines.sort()
        result_list = []

        for line in lines:
            search_term = search_term.lower()
            line_l = line.lower()
            if search_term in line_l:
                result_list.append(line)

        if len(result_list) == 0:
            print('No search results for {}'.format(search_term))
        else:
            print('Here are the results for {}:'.format(search_term))
            index = 0
            for line in result_list:
                print(' {}) {}'.format(index+1, line))
                index += 1
            print('Would you like to play any of the above? If yes, specify the number of the video.')
            print("If your answer is not a valid number, we will assume it's a no.")

            choice = input()
            if choice.isnumeric():
                for i in range(len(result_list)):
                    if int(choice) > 0 and int(choice) <= index:
                        id = result_list[int(choice)-1]
                        text1 = id.split('(')
                        text2 = text1[1].split(')')
                        self.play_video(text2[0])
                        break


    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """

        ### Getting all videos
        list_videos = self._video_library.get_all_videos()
        lines = []

        ### Getting info in videos
        for video in list_videos:
            title = video._title
            id = video._video_id
            tags = video._tags
            str_tags = ''
            tags_size = 0
            for tag in tags:
                if tags_size > 0:
                    str_tags += ' {}'.format(tag)
                    tags_size += 1
                else:
                    str_tags += '{}'.format(tag)
                    tags_size += 1

            ### Saving each line containing video info
            line = '{} ({}) [{}]'.format(
                title,
                id,
                str_tags
            )
            lines.append(line)

        ### Sorting the lines
        lines.sort()
        result_list = []

        for line in lines:
            video_tag = video_tag.lower()
            #line_l = line.lower()
            if video_tag in line:
                result_list.append(line)

        if len(result_list) == 0:
            print('No search results for {}'.format(video_tag))
        else:
            print('Here are the results for {}:'.format(video_tag))
            index = 0
            for line in result_list:
                print(' {}) {}'.format(index + 1, line))
                index += 1
            print('Would you like to play any of the above? If yes, specify the number of the video.')
            print("If your answer is not a valid number, we will assume it's a no.")

            choice = input()
            if choice.isnumeric():
                for i in range(len(result_list)):
                    if int(choice) > 0 and int(choice) <= index:
                        id = result_list[int(choice) - 1]
                        text1 = id.split('(')
                        text2 = text1[1].split(')')
                        self.play_video(text2[0])
                        break


    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")


    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
