import click
import time
from .lib import Shout

@click.command()
@click.option('--model', default='base.en', help='Model to use for transcription.')
def transcribe(model):
    s = Shout(model)
    s.start()
    try:
        while True:
            print('READ:', s.get(), '|')
            time.sleep(3)
    finally:
        s.stop()

if __name__ == '__main__':
    transcribe()