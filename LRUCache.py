class LRUCache(object):
    def __init__(self,capacity):
        #use OrderedDict to record the sequence we add into the dictionary
        self.dict1 = collections.OrderedDict;
        self.remains = capacity;
    def get(self, key):
        if key not in self.dict1:
            return -1;
        v = self.dict1.pop(key);
        #used to make it recently uesed, recently used in the tail
        self.dict1[key] = v;
        return v;

    def set(self, key, value):
        if key in self.dict1:
           self.dict1.pop(key);
        else:
           if remains >0:
             remains -=1;
           else:
             # remove the least recently used ele
               self.dict1.popitem(last = False);

        self.dict1[key] = value;
