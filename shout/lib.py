import asyncio
import numpy as np
from whispercpp import Whisper
import time
import threading
import queue
from whispercpp import audio

class Shout:
    def __init__(self, model: str = 'base.en', delay=3):
        self.model = model
        self.started = False
        self.delay = delay
        self.last_called = time.time()
        

    def start(self):
        if self.started:
            return
        self.q = queue.Queue()
        self.stop_event = threading.Event()
        self.t = threading.Thread(target=Shout.start_streaming, args=(self.q, self.model, self.stop_event))
        self.t.start()
        self.started = True

    def stop(self):
        if not self.started:
            return
        self.stop_event.set()
        self.t.join()
        self.started = False

    def get(self):
        if not self.started:
            return self.start()
        if time.time() - self.last_called < self.delay:
            time.sleep(self.delay - (time.time() - self.last_called))
        self.last_called = time.time()

        if self.q.empty():
            return None
        return self.q.get(False)

    def __del__(self):
        self.stop()

    @staticmethod
    def on_new_segment(ctx, n_new, data):
        queue, stop_event = data
        if stop_event.is_set():
            raise KeyboardInterrupt
        segment = ctx.full_n_segments() - n_new
        while segment < ctx.full_n_segments():
            queue.put(ctx.full_get_segment_text(segment))
            segment += 1

    @staticmethod
    def start_streaming(queue, model, stop_event):
        kwargs = dict(length_ms=5000, step_ms=700)
        # Load the pre-trained model.
        whisper = Whisper.from_pretrained(model)
        # Start streaming transcription from the microphone.
        ac = audio.AudioCapture(2000)
        if not ac.init_device(0, 16000):
            raise RuntimeError("Failed to initialize audio capture device.")
        whisper.params.on_new_segment(Shout.on_new_segment, (queue, stop_event))
        params = whisper.params.with_print_realtime(False).with_print_special(False).with_print_progress(False).with_token_timestamps(True)
        try:
            ac.stream_transcribe(whisper.context, params, **kwargs)
        except KeyboardInterrupt:
            return