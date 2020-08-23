import json
import requests
import urllib.parse
from secrets import spotify_user_id


class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

    def search_song(self, artist, track):
        query = urllib.parse.quote(f'{artist} {track}')
        url = f"https://api.spotify.com/v1/search?q={query}&type=track"
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        response_json = response.json()

        results = response_json['tracks']['items']
        if results:
            # let's assume the first track in the list is the song we want
            return results[0]['id']
        else:
            raise Exception(f"No song found for {artist} = {track}")

    # #### 1. Cant find where to input Spotify user ID to route to my account in Spotify_client.py            #####
    # #### 4. Change add_song_to_Spotify to a function that creates a new spotify playlist and adds it to that####
    def create_playlist(self):
        """Create A New Playlist"""
        request_body = json.dumps({
            "name": "Imported from Youtube",
            "description": "From Youtubify/ Automate to Spotify",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            spotify_user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.api_token)
            }
        )
        response_json = response.json()

        # playlist id
        return response_json["id"]

    def add_song_to_spotify(self, song_id, playlist_id):
        url = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)
        response = requests.put(
            url,
            json={
                "ids": [song_id]
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )

        return response.ok
