import spotipy

fourtet_uri = 'spotify:artist:7Eu1txygG6nJttLHbZdQOh'
spotify = spotipy.Spotify()

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
