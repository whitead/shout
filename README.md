# shout

Install

```sh
pip install git+https://github.com/whitead/shout.git
```

A simple python for getting text from input microphone.

## Quickstart

Just as a script
```sh
shout
```

In python

```py
import shout

s = shout.Shout('base.en')
text1 = s.get()
text2 = s.get()
print(text1)
s.stop()
```

## Langchain Tool
```py
from langchain.agents import Tool
import shout

s = shout.Shout()
s.start()
def wrap_shout(x):
    if 'stop' in x.casefold():
        s.stop()
        return 'Stopped'
    else:
        return s.get()
tool = Tool(
    name = "Listen to user",
    func=wrap_shout,
    description="Use this to get text from the user. Pass stop if the chain is completed, otherwise just pass listen."
)
# if you're done
s.stop()
```