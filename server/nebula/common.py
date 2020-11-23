from .constants import *

class Config(dict):
    def __init__(self):
        super(Config, self).__init__(self)
        self.update({
            "redis" : "redis://redis",
            "elastic" : ["elastic"],
            "meta_types": {}
        })

config = Config()



#
# Default values (development only)
#

config["views"] = {
    1 : {
            "title" : "Main",
            "fields" : ["id/main", "title", "subtitle", "id_folder"],
            "search" : {
                "filter" : [
                        {"terms" : {"id_folder" : [1,2]}},
                    ]
                }
    },
    2 : {
            "title" : "Fill",
            "fields" : ["id/main", "title", "id_folder"],
            "search" : {
                "filter" : [
                        {"terms" : {"id_folder" : [5,6,7,8]}},
                        {"match" : {"status" : 1}}
                    ]
                }
    },
    3 : {
            "title" : "Created last year",
            "fields" : ["id/main", "title", "id_folder", "ctime"],
            "search" : {
                "filter" : [
                        {"match" : {"status" : 1}},
                        {"range" : {"ctime" : {"lte" : "now", "gte" : "now-1y/d"}}}
                    ]
                }
    },
}



config["meta_types"] = {
}
