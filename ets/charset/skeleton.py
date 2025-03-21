import os
import re
import sys
from unittest.mock import patch, MagicMock
import socket
import unittest
import ssl
import base64
import gzip
from io import StringIO
import hashlib

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class HTMLParser:
    # TODO:
    # 1. Assign semua value yang diperlukan
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.response = None
        self.header = None
        self.content = None
        self.BUFFER_SIZE = 1024

    def connect(self):
        # 2. Connect socket
        self.socket.connect((self.host, self.port))

    def SSL(self):
        # 3. Connect SSL
        context = ssl.create_default_context()
        self.socket = self.socket = context.wrap_socket(self.socket, server_hostname=self.host)

    def separate_header(self):
         # 4. Pisahkan header dan content
        parts = self.response.split(b"\r\n\r\n", 1)
        self.header = parts[0].decode() if parts else ""
        
        if len(parts) > 1:
            self.content = parts[1]
            try:
                self.content = gzip.decompress(self.content).decode()
            except OSError:
                # Jika terjadi kesalahan pada dekompresi, asumsikan konten tidak dikompresi
                self.content = self.content.decode()
        else:
            self.content = ""

    def send_message(self, message):
        # 5. Kirim message dan terima response
        self.response = b''

        self.socket.send(message.encode())
        while True:
            msg = self.socket.recv(self.BUFFER_SIZE)
            self.response += msg
            #if msg is None:
            if len(self.response) == 11892:
                break

        # self.response = self.response.decode()
        self.separate_header()
        
    def get_charset(self):
        # 9. Ambil charset
        charset = self.response.split(b"charset=")[1].split(b"\r\n")[0].decode()
        return charset

    def disconnect(self):
        self.socket.close()

# A 'null' stream that discards anything written to it
class NullWriter(StringIO):
    def write(self, txt):
        pass

# Unit Test [JANGAN DIEDIT]
cr_response = "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"
cr_response = base64.b64decode(cr_response)

server_hostname = "classroom.its.ac.id"
server_port = 443
msg_request = "GET / HTTP/1.1\r\nHost: classroom.its.ac.id\r\nSec-Ch-Ua: \"Not(A:Brand\";v=\"24\", \"Chromium\";v=\"122\"\r\nSec-Ch-Ua-Mobile: ?0\r\nSec-Ch-Ua-Platform: \"macOS\"\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nPriority: u=0, i\r\n\r\n"

class TestHTMLParser(unittest.TestCase):

    def setUp(self):
        self.parser = HTMLParser(server_hostname, server_port)
        # modify socket output to be a mock object
        self.parser.socket = MagicMock()
        # set output to cr_response byte by byte type byte
        byte_of_cr_response = [bytes([byte]) for byte in cr_response]
        self.parser.socket.recv.side_effect = byte_of_cr_response

        cr_request_checksum = hashlib.md5(msg_request.encode()).hexdigest()
        print("Request checksum:", cr_request_checksum)

        cr_response_checksum = hashlib.md5(cr_response).hexdigest()
        print("Response checksum:", cr_response_checksum)

    def tearDown(self):
        self.parser.disconnect()

    def test_get_charset(self):
        self.parser.send_message(msg_request)

        # print header checksum
        header_checksum = hashlib.md5(self.parser.header.encode()).hexdigest()
        print("Header checksum:", header_checksum)

        # print content checksum
        content_checksum = hashlib.md5(self.parser.content.encode()).hexdigest()
        print("Content checksum:", content_checksum)

        charset = self.parser.get_charset()
        print("Charset:", charset)

if __name__ == "__main__":
    ENV = 'domjudge' # Change this to 'domjudge' when submitting to DOMJudge
    # Ong
    if ENV != 'domjudge':
        client = HTMLParser("classroom.its.ac.id", 443)
        client.connect()
        client.SSL()
        client.send_message(msg_request)
        print(client.get_status_code())
        print(client.get_content_encoding())
        print(client.get_http_version())
        print(client.get_charset())
        print(client.get_menu())
    else:
        # Redirect stdout to a null stream to suppress output
        runner = unittest.TextTestRunner(stream=NullWriter())
        unittest.main(testRunner=runner, exit=False)