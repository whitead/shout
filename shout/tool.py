"""A tool for getting audio output."""
from typing import Dict, Optional
from pydantic import Field
from langchain.tools.base import BaseTool
from .lib import Shout
import time

def _initialize_shout():
    s = Shout("base.en")
    return s

class VoiceTool(BaseTool):
    """A tool for getting transcribed speech."""
    name = "Shout transcript"
    description = "Listens to the user and transcribes their speech."
    shout_handler: Shout =  Field(default_factory=_initialize_shout())
    last_called = time.time()
    def _run(self, query: str) -> str:
        """Use the tool."""
        print("a"*100)
        s.start()
        if time.time() - self.last_called < 10:
            print(max(10, 10 - min(0,(time.time() - self.last_called))))
            time.sleep(10 - (time.time() - self.last_called))
        self.last_called = time.now()
        return self.shout_handler.get().replace("\n", "<br>")
    
    async def _arun(self, query: str) -> str:
        raise NotImplementedError("VoiceTool does not support async.")