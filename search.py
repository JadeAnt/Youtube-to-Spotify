import os
from Spotify_client import SpotifyClient
from Youtube_client import YouTubeClient

# Possible Problems/Changes
# GO THROUGH AND CONFIRM THESE AFTER WATCHING THE TUTORIAL VIDEO IN WATCH LATER
# 1. Cant find where to input Spotify user ID to route to my account in Spotify_client.py
# 2. Check if spotify.env file is being read properly
# 3. Ensure that client_secret.json is being read by Youtube_client.py
# 4. Change add_song_to_Spotify to a function that creates a new spotify playlist and adds it to that

def program():
    youtube_client = YouTubeClient('./client_secret.json')
    spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
    playlists = youtube_client.get_playlists()

    for index, playlist in enumerate(playlists):
        print(f"{index}: {playlist.title}")
    choice = int(input("Enter your choice: "))
    chosen_playlist = playlists[choice]
    print(f"You selected: {chosen_playlist.title}")

    songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
    print(f"Attempting to add {len(songs)}")

    playlist_id = spotify_client.create_playlist()

    for song in songs:
        spotify_song_id = spotify_client.search_song(song.artist, song.track)
        if spotify_song_id:
            added_song = spotify_client.add_song_to_spotify(spotify_song_id, playlist_id)
            if added_song:
                print(f"Added {song.artist} - {song.track} to your Spotify Liked Songs")


if __name__ == '__main__':
    program()
