from langchain.agents import Tool
import shout

def test_tool():
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
        description="Use this to get more input from the user. Pass stop if the chain is completed"
    )
    tool.run('freafr')
    s.stop()
    assert True