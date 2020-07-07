from config import *
from collections import OrderedDict
import json
import pprint

data = {
    "name": "ACME",
    "shares": 100,
    "price": 424.3
}

json_str = json.dumps(data)


class JSONObject:

    def __init__(self, d):
        self.__dict__ = d

    def test(self):
        print(self.name)
        print(self.shares)
        print(self.price)


json_object = json.loads(json_str, object_hook=JSONObject)

json_object.test()
print(json_object.name)
