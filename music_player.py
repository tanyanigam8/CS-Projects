import webbrowser

# Dictionary to store song names and their URLs
music_playlist = {
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
}

def play_music(song_name):
    """Plays a song from the music playlist if found."""
    song_name = song_name.lower().strip()
    if song_name in music_playlist:
        webbrowser.open(music_playlist[song_name])
        print(f"Playing {song_name}...")
    else:
        print(f"Sorry, {song_name} is not in the playlist.")

