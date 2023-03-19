import csv
from .lib import SubscriberAsync


async def log(path):
    s = SubscriberAsync()   
    while True:
        message = await s.get()
        with open(path, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
            csvwriter.writerow([message.timestamp, message.id, message.text])

def install_logger(path):
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(log(path))