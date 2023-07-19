from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import socket
import uuid
from threading import Thread
import math 
import json

server_address = "127.0.0.1:8000"
test_net_json = '{"n_layers":4,"Layers":[{"os":[2,2,1],"ni":4,"lt":0},{"os":[1,1,5],"ni":4,"lt":1,"d":{"nk":5,"kernels":[{"s":[1,1,4],"w":[-0.49915727972984314,0.063154026865959167,-0.30711203813552856,0.30829918384552002]},{"s":[1,1,4],"w":[0.084507323801517487,-0.020624732598662376,-0.15020115673542023,0.39544776082038879]},{"s":[1,1,4],"w":[0.32232806086540222,0.2460959404706955,-0.32637766003608704,0.35843029618263245]},{"s":[1,1,4],"w":[0.21092134714126587,0.013962970115244389,-0.19556853175163269,-0.48456716537475586]},{"s":[1,1,4],"w":[-0.40815180540084839,-0.13511405885219574,-0.35224428772926331,-0.33365911245346069]}],"biases":{"s":[1,1,5],"w":[0.00052689720178022981,-0.00049857597332447767,-0.00049890007358044386,-0.0005266002262942493,-0.00052658905042335391]}}},{"os":[1,1,2],"ni":5,"lt":1,"d":{"nk":2,"kernels":[{"s":[1,1,5],"w":[0.43736132979393005,-0.048073701560497284,-0.34018984436988831,-0.44259053468704224,-0.43879622220993042]},{"s":[1,1,5],"w":[-0.10869569331407547,0.027819123119115829,0.063166670501232147,0.091543465852737427,0.096374951303005219]}],"biases":{"s":[1,1,2],"w":[0.00091274973237887025,0.00038675215910188854]}}},{"os":[1,1,2],"ni":2,"lt":7}]}'

class LocalServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
    def _set_headers_json(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
    def _html(self, message):
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html("HTML SERVER TEST"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        value_str = post_data.decode("utf-8")
        message = json.loads(value_str)
        print(value_str)

        if message['t']=='request':
            if message['m']=='download':
                print("Send net to server")
                url = 'http://'+server_address+'/api/SendRequestToAgent'
                myobj = {'r':'agent', 't':'request', 'm':'upload', 'b':test_net_json}
                x = requests.post(url, json = myobj)
                print(x.text)

                #self._set_headers_json()
                #self.wfile.write(test_net_json.encode("utf8"))
            if message['m']=='upload':
                pass
            
        self._set_headers()
        self.wfile.write("".encode("utf8"))
      
def run(addr="localhost", port=8000):
    server_class=HTTPServer
    handler_class=LocalServer
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting http server on {addr}:{port}")
    httpd.serve_forever()

def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip=s.getsockname()[0]
    print("local ip: ",ip)
    s.close()
    return ip
    
if __name__ == "__main__":
    port = 8760
    ip = '127.0.0.1' #getIP()

    #start server thread
    server_thread = Thread(target=run, args=(ip, port))
    server_thread.start()
    #run(addr=ip, port=port)

    #authorization test
    mac = uuid.getnode()
    mac = ':'.join(['{:02x}'.format((mac >> elements) & 0xff) for elements in range(0,8*6,8)][::-1])#hex
    url = 'http://'+server_address+'/api/syncAgentData'
    body = {'name':'PythonAgent', 'mac':mac, 'port':port}
    myobj = {'r':'agent', 't':'info', 'm':'authorization', 'b':body}
    x = requests.post(url, json = myobj)
    print(x.text)

    #graphs test
    for i in range(1,1000):
        url = 'http://'+server_address+'/api/graphAgentDataAdd'
        sin = math.sin(math.radians(i))
        cos = math.cos(math.radians(i))
        body = {'points':{"sin":[i, sin],"cos":[i, cos]}}
        myobj = {'r':'agent', 't':'info', 'm':'loss', 'b':body}
        x = requests.post(url, json = myobj)
        print(x.text)
