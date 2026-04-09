class DLL:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.value = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {}
        self.curr = None
        self.end = None
        self.currentCapacity = 0

    def get(self, key: int) -> int:
        node = None

        if key in self.hmap and self.hmap[key]:
            node = self.hmap[key]
        else:
            return -1
        
        self.put(key, node.value)
        print(self.end.key, self.end.value)
        return node.value

    def put(self, key: int, value: int) -> None:
        # if self.end:
        #     print(self.end.key)
        if key in self.hmap and self.hmap[key]:
            self.remove(self.hmap[key])
            self.insert(key, value)
        else:
            if self.currentCapacity == self.capacity:
                # print(self.end.key)
                self.remove(self.end)
                # print(self.end.key)
                self.currentCapacity -= 1
            self.insert(key, value)
            self.currentCapacity += 1


    
    def remove(self, node):

        pre = node.prev
        nex = node.next

        node.prev = None
        node.next = None
        
        self.hmap[node.key] = None
        if nex:
            nex.prev = pre
        else:
            self.end = pre

        if pre:
            pre.next = nex
        else:
            self.curr = nex

    
    def insert(self, key, val):
        node = DLL(key, val)
        
        if self.curr:
            self.curr.prev = node
            node.next = self.curr
        
        if not self.end:
            self.end = node
        
        self.curr = node

        self.hmap[key] = self.curr
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)