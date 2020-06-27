
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = '0e92a854dd28455fbb9a1c91ea9787d4'
CLIENT_ID_SECRET = '2b88d74df8bc4500940b46cb9183e02f' #NEED TO FIGURE OUT HOW TO REMOVE THIS AND GET IT WORKING ON ANY DEVICE


artist_uri = 'spotify:track:7f8iBUiwio1oX5lAFwC5xI' #Enter any artist URI here

client_credentials_manager = SpotifyClientCredentials(client_id = CLIENT_ID, client_secret = CLIENT_ID_SECRET)

spotify = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

results = spotify.artist_top_tracks(artist_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()