import random
import string
import webbrowser
import urlparse
import requests
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class OAuthWebFlowController():
    
    class RequestHandler(BaseHTTPRequestHandler):
        
        def __init__(_self, *args, **kwargs):
            BaseHTTPRequestHandler.__init__(_self, *args, **kwargs)

        def log_message(_self, format, *args):
            return

        def do_GET(_self):
            code = _self.parse_temp_code(_self.path)

            _self.send_response(200)
            _self.send_header("Content-type", "text/plain")
            _self.end_headers()
            _self.wfile.write("Code: %s" % code)
            _self.wfile.close()

    def __init__(self, client_id, client_secret, redirect_uri, scope, port=5555):
        self.state = self.random_state(16)
        self.code = ''
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.port = port
        OAuthWebFlowController.RequestHandler.parse_temp_code = self.parse_temp_code

    def random_state(self, length):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

    #override
    def parse_temp_code(self, path):
        qs = urlparse.urlparse(path).query
        parsed_qs = urlparse.parse_qs(qs)
        self.code = parsed_qs['code'][0]
        return self.code

    #override
    def authorization_url(self):
        return ''

    #override
    def temp_code_to_access_code(self):
        return None

    def get_temp_auth_code(self):
        webbrowser.open_new(self.authorization_url());
        server = HTTPServer(('', self.port), OAuthWebFlowController.RequestHandler)
        server.handle_request()
        server.server_close()
        return self.code

    def get_access_code(self):
        temp_code = self.get_temp_auth_code()
        return self.temp_code_to_access_code()

class GoogleOAuth(OAuthWebFlowController):
    
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        OAuthWebFlowController.__init__(self, client_id, client_secret, redirect_uri, scope)

    #override
    def authorization_url(self):
        url = 'https://accounts.google.com/o/oauth2/v2/auth'
        data = {
            'client_id': self.client_id,
            'response_type': 'code',
            'redirect_uri': self.redirect_uri,
            'scope': self.scope,
            'state': self.state
        }
        req = requests.Request('GET', url, data=data)
        prepped = req.prepare()
        
        return prepped.url + '?' + prepped.body

    #override
    def temp_code_to_access_code(self):
        url = 'https://www.googleapis.com/oauth2/v4/token'
        headers = {'Accept': 'application/json'}
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': self.code,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code'
        }
        r = requests.post(url, headers=headers, data=data)
        return r.json()

class GithubOAuth(OAuthWebFlowController):
    
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        OAuthWebFlowController.__init__(self, client_id, client_secret, redirect_uri, scope)

    #override
    def authorization_url(self):
        url = 'https://github.com/login/oauth/authorize'
        data = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'scope': self.scope,
            'state': self.state
        }
        req = requests.Request('GET', url, data=data)
        prepped = req.prepare()
        
        return prepped.url + '?' + prepped.body

    #override
    def temp_code_to_access_code(self):
        url = 'https://github.com/login/oauth/access_token'
        headers = {'Accept': 'application/json'}
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': self.code,
            'redirect_uri': self.redirect_uri,
            'state': self.state
        }
        r = requests.post(url, headers=headers, data=data)
        return r.json()

class FacebookOAuth(OAuthWebFlowController):
    
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        OAuthWebFlowController.__init__(self, client_id, client_secret, redirect_uri, scope)

    #override
    def authorization_url(self):
        url = 'https://www.facebook.com/dialog/oauth'
        data = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'scope': self.scope,
            'state': self.state
        }
        req = requests.Request('GET', url, data=data)
        prepped = req.prepare()
        
        return prepped.url + '?' + prepped.body

    #override
    def temp_code_to_access_code(self):
        url = 'https://graph.facebook.com/v2.3/oauth/access_token'
        headers = {'Accept': 'application/json'}
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': self.code,
            'redirect_uri': self.redirect_uri,
            'state': self.state
        }
        r = requests.post(url, headers=headers, data=data)
        return r.json()

class SpotifyOAuth(OAuthWebFlowController):
    
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        OAuthWebFlowController.__init__(self, client_id, client_secret, redirect_uri, scope)

    #override
    def authorization_url(self):
        url = 'https://accounts.spotify.com/authorize'
        data = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'scope': self.scope,
            'state': self.state,
            'response_type': 'code'
        }
        req = requests.Request('GET', url, data=data)
        prepped = req.prepare()
        
        return prepped.url + '?' + prepped.body

    #override
    def temp_code_to_access_code(self):
        url = 'https://accounts.spotify.com/api/token'
        headers = {'Accept': 'application/json'}
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': self.code,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code'
        }
        r = requests.post(url, headers=headers, data=data)
        return r.json()
