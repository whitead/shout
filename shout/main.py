import click
from .lib import Subscriber
from .tools import install_logger

@click.command()
@click.option('-f', '--file', default=None)
def main(file=None):
    s = Subscriber()
    print('Connected...')
    if file is not None:
        install_logger(file)
    while True:
        message = s.get()
        print(message.timestamp, message.text)