import json
import socket
from config import ENCODING

def receive_data(socket: socket.socket):
    header = recv_exact(socket, 4)
    length = int.from_bytes(header)
    
    payload = recv_exact(socket, length)
    payload_text = payload.decode(ENCODING)
    payload_json = json.loads(payload_text)
    
    
def recv_exact(socket: socket.socket, length:int):
    data:bytes = bytes()
    while len(data) < length:
        chunk = socket.recv(length - len(data))
        if chunk == b'':
            raise Exception("Connection Closed")
        
        data += chunk
    return data