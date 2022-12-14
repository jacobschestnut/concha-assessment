from hashlib import new
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib import response
from views import get_all_users, get_single_user, create_user, update_user, delete_user, get_user_by_first_name, get_user_by_last_name, get_user_by_email, get_user_by_address
from views import get_all_sessions, get_single_session, update_session, create_session

class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        path_params = path.split('/')
        resource = path_params[1]

        if '?' in resource:

            param = resource.split('?')[1]
            resource = resource.split('?')[0]
            pair = param.split('=')
            key = pair[0]
            value = pair[1]

            return (resource, key, value)

        else:
            id = None
            try:
                id = int(path_params[2])
            except (IndexError, ValueError):
                pass
            return (resource, id)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        self._set_headers(200)
        response = {}
        parsed = self.parse_url(self.path)
        
        if len(parsed) ==2:
            ( resource, id ) = parsed
            
            if resource == "users":
                if id is not None:
                    response = f"{get_single_user(id)}"
                else:
                    response = f"{get_all_users()}"
                    
            elif resource == "sessions":
                if id is not None:
                    response = f"{get_single_session(id)}"
                else:
                    response = f"{get_all_sessions()}"
                    
        elif len(parsed) == 3:
            ( resource, key, value ) = parsed

            if key == "firstname" and resource == "users":
                response = get_user_by_first_name(value)
                
            if key == "lastname" and resource == "users":
                response = get_user_by_last_name(value)
                
            if key == "address" and resource == "users":
                response = get_user_by_address(value)
                
            if key == "email" and resource == "users":
                response = get_user_by_email(value)  

        self.wfile.write(response.encode())

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''

        (resource, input) = self.parse_url(self.path)

        if resource == "users":
            response = create_user(post_body)
            
        elif resource == "sessions":
            response = create_session(post_body)
            
        self.wfile.write(response.encode())

    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "users":
            success = update_user(id, post_body)
            
        if resource == "sessions":
            success = update_session(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    def do_DELETE(self):
   
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        if resource == "users":
            delete_user(id)

        self.wfile.write("".encode())
        
def main():
    """Starts the server on port 8000 using the HandleRequests class
    """
    host = ''
    port = 8000
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()