class HashTable:
    def __init__(self):
        self.collection={}
    def hash(self,s):
        hashed_value=0
        for character in s:
            hashed_value+=ord(character)
        return hashed_value
    def add(self,key,value):
        hashed_key=self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key]={}
        self.collection[hashed_key][key]=value
    def remove(self,key):
        hashed_key=self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]

                # Remove empty bucket
                if not self.collection[hashed_key]:
                    del self.collection[hashed_key]
        
    def lookup(self,key):
        hashed_key=self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                return self.collection[hashed_key][key]
        
        return None
        