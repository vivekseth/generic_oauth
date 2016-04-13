import _secrets
import requests
from generic_oauth import SpotifyOAuth

def api_call(access_data, endpoint):
	headers = {
		'Authorization': 'Bearer ' + access_data['access_token']
	}
	base_url = 'https://api.spotify.com/v1'
	endpoint = endpoint

	r = requests.get(base_url + endpoint, headers=headers)
	return r.json()

o = SpotifyOAuth(secrets.client_id, secrets.client_secret, secrets.redirect_uri, secrets.scope_string)
access_data = o.get_access_code()
print api_call(access_data, '/me')
