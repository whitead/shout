# shout

This is a client for [whisper.cpp with ZMQ](github.com/whitead/whisper.cpp).

Install

```sh
pip install git+https://github.com/whitead/shout.git
```

Install ZMQ whisper server

```sh
git clone https://github.com/whitead/whisper.cpp
cd whisper.cpp
make streammq
streammq --step -1 
```

## Quickstart

Ensure you have a running ZMQ whisper server.

```py
import shout

s = shout.Subscriber()

print(s.get())

```

### Asynchronous

```py
import shout

async def func():
    s = shout.SubscriberAsync()
    print(await s.get())

```