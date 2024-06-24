import os
import socket
import select
import sys
import unittest
from unittest.mock import patch, MagicMock
import base64, hashlib
from io import StringIO

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class HTTPServer:
    def __init__(self, host, port):
        self.server_socket = None
        self.host = ?
        self.port = ?

    def handle_request(self, path):
        print("HANDLE REQUEST", path)
        # HINT:: >> IF path is a directory, return the list of files in the directory

        if path == 'index.html' or path == '/' or path == '/index.html':
            ?
            
            content_length = ?
            response_header = ?

            return ?

        if path[0] == '/':
            path = path[1:]

        abs_path = os.path.join(BASE_DIR, path)

        # print("ABS PATH", abs_path)
        if os.path.isdir(abs_path):
            # Show directory contents
            dir_contents = os.listdir(abs_path)
            dir_list = []
            for f in range(len(dir_contents)):
                ?

            response_data = ''
            for f in range(len(dir_list)):
                ?

            content_length = ?
            response_header = ?

            return ?

        elif os.path.exists(abs_path):
            if path.endswith('.html'):
                # Read html file and send to client
                ?

                content_length = ?
                response_header = ?

                return ?
            else:
                # Read other file types and send to client as download
                ?

                content_length = ?
                response_header = ?

                return ?
        else:
            # Return 404
            ?

            content_length = ?
            response_header = ?

            return ?

    def start(self):
        self.server_socket = ?
        ?

        print(f'Server is listening on {self.host}:{self.port}')

        input_socket = [self.server_socket]

        try:
            while True:
                read_ready, write_ready, exception = ?

                for sock in read_ready:
                    if sock == self.server_socket:
                        ?
                    else:
                        ?

                        request_header = data
                        request_file = request_header.split()[1]
                        response_header = b''
                        response_data = b''

                        # ATTENTION: PLEASE DO NOT CHANGE CODE BELOW THIS LINE
                        if '/exit' in data:
                            sock.sendall(b'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n')
                            return
                        # ATTENTION: PLEASE DO NOT CHANGE CODE ABOVE THIS LINE

                        # send response header and data
                        response_header, response_data = ?
                        sock.sendall(response_header + response_data)

        except KeyboardInterrupt:
            self.server_socket.close()
            sys.exit(0)

    def stop(self):
        print("Shutting down server...")
        self.server_socket.close()
        sys.exit(0)

INDEX_HTML = base64.b64decode('PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KICA8aGVhZD4KICAgIDxtZXRhIGNoYXJzZXQ9IlVURi04IiAvPgogICAgPG1ldGEgaHR0cC1lcXVpdj0iWC1VQS1Db21wYXRpYmxlIiBjb250ZW50PSJJRT1lZGdlIiAvPgogICAgPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlhbC1zY2FsZT0xLjAiIC8+CiAgICA8dGl0bGU+RG9jdW1lbnQ8L3RpdGxlPgogIDwvaGVhZD4KICA8Ym9keT4KICAgIGhlbGxvIHdvcmxkCiAgICA8c2NyaXB0PgogICAgICBzZXRUaW1lb3V0KCgpID0+IHsKICAgICAgICB3aW5kb3cubG9jYXRpb24uaHJlZiA9ICJodHRwczovL2l0cy5pZC9tL18iOwogICAgICB9LCA1MDAwKTsKICAgIDwvc2NyaXB0PgogIDwvYm9keT4KPC9odG1sPg==').decode('utf-8')
SAMPLE_HTML = base64.b64decode('PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KICA8aGVhZD4KICAgIDxtZXRhIGNoYXJzZXQ9IlVURi04IiAvPgogICAgPG1ldGEgaHR0cC1lcXVpdj0iWC1VQS1Db21wYXRpYmxlIiBjb250ZW50PSJJRT1lZGdlIiAvPgogICAgPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlhbC1zY2FsZT0xLjAiIC8+CiAgICA8dGl0bGU+RG9jdW1lbnQ8L3RpdGxlPgogIDwvaGVhZD4KICA8Ym9keT4KICAgIEhlbGxvLCBzYW1wbGUKICAgIDxzY3JpcHQ+CiAgICAgIHNldFRpbWVvdXQoKCkgPT4gewogICAgICAgIHdpbmRvdy5sb2NhdGlvbi5ocmVmID0gImh0dHBzOi8vaXRzLmlkL20vXyI7CiAgICAgIH0sIDUwMDApOwogICAgPC9zY3JpcHQ+CiAgPC9ib2R5Pgo8L2h0bWw+').decode('utf-8')
NOTFOUND_HTML = base64.b64decode('PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KICA8aGVhZD4KICAgIDxtZXRhIGNoYXJzZXQ9IlVURi04IiAvPgogICAgPG1ldGEgaHR0cC1lcXVpdj0iWC1VQS1Db21wYXRpYmxlIiBjb250ZW50PSJJRT1lZGdlIiAvPgogICAgPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlhbC1zY2FsZT0xLjAiIC8+CiAgICA8dGl0bGU+RG9jdW1lbnQ8L3RpdGxlPgogIDwvaGVhZD4KICA8Ym9keT4KICAgIDQwNCBOb3QgRm91bmQKICAgIDxzY3JpcHQ+CiAgICAgIHNldFRpbWVvdXQoKCkgPT4gewogICAgICAgIHdpbmRvdy5sb2NhdGlvbi5ocmVmID0gImh0dHBzOi8vaXRzLmlkL20vXyI7CiAgICAgIH0sIDUwMDApOwogICAgPC9zY3JpcHQ+CiAgPC9ib2R5Pgo8L2h0bWw+').decode('utf-8')
IMAGE_PNG = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAJYAAACWAQMAAAAGz+OhAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABIklEQVRIicWVS46EMAxEC7HIkiNwE3KzZlBfDG6SI2SZBcLjivs3vY4zllqC14uYcpUDdKggWnkofMgrXzqxBIw5lsi/btpI9GAi9zzocfOYb5OUrizyEXBlCLukzow6L2EP39o3ZNUvyopq+sdDvuxVkiR/B8WRsZe7/rQXTBub8mCYf6AZVLll41D7MK1ZWymxwASX9iykUV0UnxnczVf+DLUFy+V0TYd5qC0L6ZxPDLLry2uWXRgzcXGoJ1a5TOfWrGpamAXZ5FNnZyZptXywqYOG7cGsljrorBOGA7O9pj4toE+P965zZol7nOtb8/HspTmr9yCPM01jV8aNU+9BES+2VHH52e9zvVm9f/HIxwUP9vAL7yNdM/LpIU/2T/UL8CUYrMvxa7kAAAAASUVORK5CYII=')

def PARSE_HEADER(data):
    headers = {}
    lines = data.split('\r\n')
    for line in lines:
        parts = line.split(': ')
        if len(parts) == 2:
            headers[parts[0]] = parts[1]
    return headers

class TestHTTPServer(unittest.TestCase):
    @patch('builtins.open')
    @patch('socket.socket')
    @patch('select.select')
    def test_handle_request_index1(self, mock_select, mock_socket, mock_open):
        server = HTTPServer('localhost', 8080)
        mock_socket.return_value = MagicMock()
        mock_socket.return_value.recv.return_value = b'GET /index.html HTTP/1.1'
        mock_open.return_value = MagicMock()
        mock_open.return_value.read.return_value = INDEX_HTML
        mock_select.return_value = ([mock_socket], [], [])
        response_header, response_data = server.handle_request('index.html')
        # parse response header
        response_header = response_header.decode('utf-8')
        response_header = PARSE_HEADER(response_header)

        self.assertIn('text/html', response_header['Content-Type'])
        print("Content-Type: OK")
        
        self.assertEqual(response_data.decode('utf-8'), INDEX_HTML)
        hash_data = hashlib.sha256(response_data).hexdigest()
        print("Response hash: ", hash_data)

    @patch('builtins.open')
    @patch('socket.socket')
    @patch('select.select')
    def test_handle_request_index2(self, mock_select, mock_socket, mock_open):
        server = HTTPServer('localhost', 8080)
        mock_socket.return_value = MagicMock()
        mock_socket.return_value.recv.return_value = b'GET / HTTP/1.1'
        mock_open.return_value = MagicMock()
        mock_open.return_value.read.return_value = INDEX_HTML
        mock_select.return_value = ([mock_socket], [], [])
        response_header, response_data = server.handle_request('/')
        # parse response header
        response_header = response_header.decode('utf-8')
        response_header = PARSE_HEADER(response_header)

        self.assertIn('text/html', response_header['Content-Type'])
        print("Content-Type: OK")
        
        self.assertEqual(response_data.decode('utf-8'), INDEX_HTML)
        hash_data = hashlib.sha256(response_data).hexdigest()
        print("Response hash:", hash_data)

    # TEST GET /dataset/, mock isdir
    @patch('builtins.open')
    @patch('socket.socket')
    @patch('select.select')
    @patch('os.listdir')
    @patch('os.path.isdir')
    def test_handle_request_dir(self, mock_isdir, mock_listdir, mock_select, mock_socket, mock_open):
        server = HTTPServer('localhost', 8080)
        mock_socket.return_value = MagicMock()
        mock_socket.return_value.recv.return_value = b'GET /dataset/ HTTP/1.1'
        mock_open.return_value = MagicMock()
        mock_isdir.return_value = True
        mock_listdir.return_value = ['0.png', '1.txt', '2.pdf', '3.html', '4.zip']
        mock_select.return_value = ([mock_socket], [], [])
        response_header, response_data = server.handle_request('dataset/')
        # parse response header
        response_header = response_header.decode('utf-8')
        response_header = PARSE_HEADER(response_header)

        self.assertIn('text/html', response_header['Content-Type'])
        print("Content-Type: OK")

        expected = "<li><a href=\"\"/>0.png</li>\n<li><a href=\"\"/>1.txt</li>\n<li><a href=\"\"/>2.pdf</li>\n<li><a href=\"\"/>3.html</li>\n<li><a href=\"\"/>4.zip</li>\n"
        print("Response data:", expected)
        self.assertEqual(response_data.decode('utf-8'), expected)

    # TEST DOWNLOAD /dataset/0.png, mock read
    @patch('builtins.open')
    @patch('socket.socket')
    @patch('select.select')
    @patch('os.path.exists')
    def test_handle_request_image(self, mock_exists, mock_select, mock_socket, mock_open):
        server = HTTPServer('localhost', 8080)
        mock_socket.return_value = MagicMock()
        mock_socket.return_value.recv.return_value = b'GET /dataset/0.png HTTP/1.1'
        mock_open.return_value = MagicMock()
        mock_open.return_value.read.return_value = IMAGE_PNG
        mock_exists.return_value = True
        mock_select.return_value = ([mock_socket], [], [])
        response_header, response_data = server.handle_request('dataset/0.png')
        # parse response header
        response_header = response_header.decode('utf-8')
        response_header = PARSE_HEADER(response_header)

        self.assertIn('application/octet-stream', response_header['Content-Type'])
        print("Content-Type: OK")
        
        self.assertEqual(response_data, IMAGE_PNG)
        hash_data = hashlib.sha256(response_data).hexdigest()
        print("Response hash:", hash_data)


    # TEST /dataset/3.html
    @patch('builtins.open')
    @patch('socket.socket')
    @patch('select.select')
    def test_handle_request_html(self, mock_select, mock_socket, mock_open):
        server = HTTPServer('localhost', 8080)
        mock_socket.return_value = MagicMock()
        mock_socket.return_value.recv.return_value = b'GET /dataset/3.html HTTP/1.1'
        mock_open.return_value = MagicMock()
        mock_open.return_value.read.return_value = SAMPLE_HTML
        mock_select.return_value = ([mock_socket], [], [])
        response_header, response_data = server.handle_request('dataset/3.html')
        # parse response header
        response_header = response_header.decode('utf-8')
        response_header = PARSE_HEADER(response_header)

        self.assertIn('text/html', response_header['Content-Type'])
        print("Content-Type: OK")
        
        self.assertEqual(response_data.decode('utf-8'), SAMPLE_HTML)
        hash_data = hashlib.sha256(response_data).hexdigest()
        print("Response hash:", hash_data)

    # TEST 404
    @patch('builtins.open')
    @patch('socket.socket')
    @patch('select.select')
    def test_handle_request_404(self, mock_select, mock_socket, mock_open):
        server = HTTPServer('localhost', 8080)
        mock_socket.return_value = MagicMock()
        mock_socket.return_value.recv.return_value = b'GET /notfound.html HTTP/1.1'
        mock_open.return_value = MagicMock()
        mock_open.return_value.read.return_value = NOTFOUND_HTML
        mock_select.return_value = ([mock_socket], [], [])
        response_header, response_data = server.handle_request('notfound.html')
        # parse response header
        response_header = response_header.decode('utf-8')
        response_header = PARSE_HEADER(response_header)

        self.assertIn('text/html', response_header['Content-Type'])
        print("Content-Type: OK")
        
        # status_code = response_header.split()[1]
        # self.assertEqual(status_code, '404')
        
        self.assertEqual(response_data.decode('utf-8'), NOTFOUND_HTML)
        hash_data = hashlib.sha256(response_data).hexdigest()
        print("Response hash:", hash_data)

# A 'null' stream that discards anything written to it
class NullWriter(StringIO):
    def write(self, txt):
        pass

if __name__ == '__main__':
    # ENV = 'domjudgex' # Change this to 'domjudge' when submitting to DOMJudge
    # if ENV != 'domjudge':
    #     # unittest.main()
    #     runner = unittest.TextTestRunner(stream=NullWriter())
    #     unittest.main(testRunner=runner, exit=False)
    # else:
        # config = (open(os.path.join(BASE_DIR, 'httpserver.conf'), 'r').read().split('\n'))
        # # print(config[1])
        # PORT = str(config[0]).replace('PORT=', '')
        # HOST = str(config[1]).replace('HOST=', '')
    server = HTTPServer('localhost', 8080)
    server.start()
    server.stop()