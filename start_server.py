from gevent.pywsgi import WSGIServer
from app import create_app

print("WIKIPI version 0.5 beta.")
print("gevent server started at http://localhost:3600")
http_server = WSGIServer(('0.0.0.0', 3600), create_app())
http_server.serve_forever()