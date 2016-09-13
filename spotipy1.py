import spotipy
import spotipy.util as util

#Here is the flow of the app: 
#0. Authenticate with Spotify credentials
#1. Find track playing now
#2. Find tracks with similar genre, key, BPM
#3. Find tracks that match some of the criteria (P2)
#4. Offer choice and queue the chosen track

username = 'guygilbert66'
scope = 'user-library-read'
client_id = '261fdbf599a4419291e83c05ddadf224'
client_secret = '6e1bc3b96d9842c4a445039882879606'
redirect_uri = 'http://192.168.1.31/'

token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)

if token:
	sp = spotipy.Spotify(auth=token)
	results = sp.current_user_saved_tracks(2)
	for item in results['items']:
		track = item['track']
		print(track['name'] + ' - ' + track['artists'][0]['name'])
	recos = sp.recommendations(seed_genres=['deep-house','chill'],limit=3,country='US')
	for item in recos['tracks']:
		track = item['track_number']
		print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)

