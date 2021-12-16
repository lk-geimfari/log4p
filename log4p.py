import connector

class Logger:
    def __init__(self, remote=False, **kwargs):
        if not remote:
            self.log = exec
        else:
            c = connector.Client(kwargs["address"])
            self.log = c.log
