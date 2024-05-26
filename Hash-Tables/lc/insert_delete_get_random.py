class RandomizedSet(object):

    def __init__(self):
        self.dict = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.dict[val] = 1
            return True
        else: 
            return False
        
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            del self.dict[val]
            return True
        return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.dict.keys())
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()