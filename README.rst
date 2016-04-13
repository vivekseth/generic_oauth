# Generic Oauth

## Description

`generic_oauth` makes it extremely simple to use any OAuth v2 API purely from the command line. With any of the provided implementations you can get an access token in just 2 lines of code.

Typically browsers are a required component of the Oauth flow—APIs use html pages to allow users to grant permisson to third party apps to make requests on their behalf. This makes it easy for web-apps to use oauth apis, but difficult and clunkly for command-line apps to use these services. 

With `generic_oauth` you can synchronosly generate access_tokens for any oauth api with just a few lines of code. 

Implementations included: 

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

## How to include in project

TODO


