# Generic Oauth

## Description

`generic_oauth` provides synchronous OAuth 2.0 authentication for command-line python programs.  With any of the provided implementations you can get an access token for an OAuth service in just 2 lines of code.

To install use: `pip install generic_oauth`

Typically, OAuth services are used by web-apps becuase the protocol requires use of a browser. This can be frustrating for people who want to build simple, command-line programs that use OAuth APIs. Let's say you want to use Spotify's API, to get data on the music you listen to. You shouldnt have to build a web-app first. Using `generic_oauth` you can authenticate your app to use an OAuth API directly from your python program. 

The following implementations included: 

- Google
- Github
- Facebook
- Spotify

## Sample Usage

```
import secrets
import requests
from generic_oauth import SpotifyOAuth

# Get a spotify access_token in just 2 lines. 
o = SpotifyOAuth(secrets.client_id, secrets.client_secret, secrets.redirect_uri, secrets.scope_string)
access_data = o.get_access_code()

headers = {'Authorization': 'Bearer ' + access_data['access_token']}
r = requests.get('https://api.spotify.com/v1/me', headers=headers)
print r.json()

```

## Documentation

`OAuthWebFlowController` is an abstract class responsible for handling the bulk of the oauth 2.0 web flow. To implement a handler for an OAuth api not already included, you will need to make a subclass of this class and override the `authorization_url()` and `parse_temp_code()` methods.

`OAuthWebFlowController` creates a temporarly local HTTP server to accept data sent to the `redirect_uri`. The default `redirect_uri` supported is http://localhost:5555. If you would like to use a different url, you will need to change the `port` param in the `__init__` method. For example if you use http://localhost:4321, you would set port=4321. 











