class DLL:

    def __init__(self, val):
        self.val = val
        self.key = None
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.currentCapacity = 0
        self.capacity = capacity
        self.map = {}
        self.end = None
        self.start = None


    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.add(node)
            return self.map[key].val
        
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            node.val = value
            self.add(node)
            return
        if self.currentCapacity == self.capacity:
            if self.start:
                del self.map[self.start.key]
                self.remove(self.start)
                self.currentCapacity -= 1
        
        node = DLL(value)
        node.key = key
        self.add(node)
        self.map[key] = node
        self.currentCapacity += 1


    def remove(self, node):
        if not node:
            return
        prev = node.prev
        nex = node.next

        node.prev = None
        node.next = None
        if prev:
            prev.next = nex
        else:
            self.start = nex
        if nex:
            nex.prev = prev
        else:
            self.end = prev
    
    def add(self, node):
        if not self.end:
            self.end = node
            self.start = node
            return
        
        self.end.next = node
        node.prev = self.end
        self.end = node
        
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)