class MyHashMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 100
        self.data = [{} for i in range(self.capacity)]  # 链地址法 用平衡二叉树
    
    @staticmethod
    def _hash(key):
        return key % 100
    
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.data[self._hash(key)][key] = value
    
    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if key in self.data[self._hash(key)]:
            return self.data[self._hash(key)][key]
        else:
            return -1
    
    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        if key in self.data[self._hash(key)]:
            self.data[self._hash(key)].pop(key)
    
    
if __name__ == '__main__':
    key, value = 3, 2
    
    obj = MyHashMap()
    obj.put(key, value)
    
    # <editor-fold desc="debug">
    print(obj.data)
    # </editor-fold>
    
    param_2 = obj.get(key)
    obj.remove(key)

    # <editor-fold desc="debug">
    print(obj.data)
    # </editor-fold>