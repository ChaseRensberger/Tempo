
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = '0e92a854dd28455fbb9a1c91ea9787d4'
CLIENT_ID_SECRET = '2b88d74df8bc4500940b46cb9183e02f'

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

client_credentials_manager = SpotifyClientCredentials(client_id = CLIENT_ID, client_secret = CLIENT_ID_SECRET)

spotify = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


results = spotify.artist_albums(birdy_uri, album_type = 'album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])