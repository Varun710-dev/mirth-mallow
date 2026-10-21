from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PORT = 8000
handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))

with ThreadingHTTPServer(("127.0.0.1", PORT), handler) as server:
    print("Application started", flush=True)
    print(f"Open: http://localhost:{PORT}", flush=True)
    print("Press Ctrl+C to stop the server.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nApplication stopped.", flush=True)
