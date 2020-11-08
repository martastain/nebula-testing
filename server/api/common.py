class Config(dict):
    def __init__(self):
        super(Config, self).__init__(self)
        self.update({
            "redis" : "redis://redis",
            "elastic" : ["elastic"]
        })

config = Config()
