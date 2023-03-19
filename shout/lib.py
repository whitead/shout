import asyncio
import zmq
import zmq.asyncio
import dataclasses
from datetime import datetime

from dataclasses import dataclass

@dataclass
class Message:
    timestamp: str
    id: int
    start: str
    duration: str
    text: str


class Subscriber:
    
    def __init__(self, url='tcp://localhost:5749'):
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.connect(url)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "")
    
    def get(self, block=True):
        s = self.socket.recv_string(flags=zmq.NOBLOCK if not block else 0)
        try:
            i, s, d, t = s.split('|')
        except ValueError:
             return Message(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0, '', '', s)
        return Message(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), i, s, d, t)


class SubscriberAsync:
    
    def __init__(self, url='tcp://localhost:5749'):
        context = zmq.asyncio.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.connect(url)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "")
    
    async def get(self):
        s = self.socket.recv_string()
        i, s, d, t = s.split('|')
        return Message(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), i, s, d, t)



