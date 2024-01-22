import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, SPOTIPY_USERNAME

# Set the scope for the requested permissions
SCOPE = 'user-library-read user-top-read'

# Create a SpotifyOAuth object
sp_oauth = SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=SCOPE, username=SPOTIPY_USERNAME)

# Get the token
token_info = sp_oauth.get_cached_token()

if not token_info:
    auth_url = sp_oauth.get_authorize_url()
    print(f'Please navigate to this URL: {auth_url}')
    response = input('Enter the URL you were redirected to: ')

    token_info = sp_oauth.get_access_token(response)

# Create a Spotipy object using the token
sp = spotipy.Spotify(auth=token_info['access_token'])

# Get user's top artists and tracks
top_artists = sp.current_user_top_artists(limit=5, time_range='medium_term')
top_tracks = sp.current_user_top_tracks(limit=5, time_range='medium_term')

# Print the results
print("Your Top 5 Artists:")
for i, artist in enumerate(top_artists['items'], 1):
    print(f"{i}. {artist['name']}")

print("\nYour Top 5 Tracks:")
for i, track in enumerate(top_tracks['items'], 1):
    print(f"{i}. {track['name']} by {track['artists'][0]['name']}")
