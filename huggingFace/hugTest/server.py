from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import json
import subprocess
import time
from urllib.parse import quote
import socket 

''' my function'''
from getTranscript import getTranscript

port = 8000
hostname=socket.gethostname()
ipAddr = socket.gethostbyname(hostname)

print(f"Serving from: http://{hostname}.local:{port}")
print(f"at IP: http://{ipAddr}:{port}")


''' Function to convert the post data to an array for easier use'''
def postDataToArray(postData):
    raw_text = postData.decode("utf8")
    print("Raw")
    data = json.loads(raw_text)
    return data


''' Handle GET and POST requests to the server'''
class uHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))
        except:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 - Not Found')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = postDataToArray(post_data)
        '''
        data consists of 
            data['action'] and 
            data['value']
        '''
        self._set_headers()
        print(data)
        rData = {}
        rData['item'] = ""
        rData['status'] = ""
        
        

        if data['action'] == "showTranscript":
            transcript = getTranscript()
            rData['item'] = "transcript"
            rData['status'] = transcript

 

        self.wfile.write(bytes(json.dumps(rData), 'utf-8'))




httpd = HTTPServer(('', port), uHTTPRequestHandler)
# httpd.serve_forever()

while True:
    httpd.handle_request()
    time.sleep(0.1)


# while True:
#     httpd.handle_request()
#     now = time.localtime()
#     print(f"Time: {now.tm_hour}:{now.tm_min} | {alarmTime.hr}:{alarmTime.min}")
#     if (now.tm_hour == alarmTime.hr) and (now.tm_min == alarmTime.min) and not alarmOn:
#         print("We have alarm!")
#         alarmOn = True 
#         rhythmboxCommand("play")
