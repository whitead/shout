import click
from .lib import Subscriber

@click.command()
def main(args=None):
    s = Subscriber()
    print('Connected...')
    while True:
        message = s.get()
        print(message.timestamp, message.text)