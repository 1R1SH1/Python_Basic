class MyDict(dict):
    def __init__(self, *args, **kw):
        super(MyDict, self).__init__(*args, **kw)

    def __missing__(self, key):
        return 0

    def get(self, key):
        return self.__getitem__(key)

d = MyDict({"a": 1, "b": 2})
print(d.get("a"))
print(d.get("c"))
