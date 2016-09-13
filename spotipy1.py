import spotipy

#Here is the flow of the app: 
#1. Find track playing now
#2. Find tracks with similar genre, key, BPM
#3. Find tracks that match some of the criteria
#4. Offer choice and queue the chosen track

fourtet_uri = 'spotify:artist:7Eu1txygG6nJttLHbZdQOh'
spotify = spotipy.Spotify()

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
