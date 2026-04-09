class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.value = val
        self.prev = prev
        self.next = next
        self.freq = 1

class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1 ,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        #key -> (node)
        self.hmap = {}
        #freq -> list
        self.freq = {}
        self.min_freq = 1
        self.currentCapacity = 0

    def get(self, key: int) -> int:
        node = None
        if key in self.hmap and self.hmap[key]:
            node = self.hmap[key]
        else:
            return -1
        
        # print(node.key, node.prev.key)
        self.remove(node)
        # print(self.freq[1].head.next.key)
        if node.freq == self.min_freq and self.freq[node.freq].head.next.key == -1:
            self.min_freq += 1
        self.insert(node, node.freq + 1)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hmap and self.hmap[key]:
            node = self.hmap[key]
            node.value = value
            self.remove(node)
            if node.freq == self.min_freq and self.freq[node.freq].head.next.key == -1:
                self.min_freq += 1
            self.insert(node, node.freq + 1)
        else:
            if self.currentCapacity == self.capacity:
                victim = self.freq[self.min_freq].tail.prev
                self.remove(victim)
                self.hmap[victim.key] = None 
                self.currentCapacity -= 1
            self.insert(Node(key, value), 1)
            self.currentCapacity += 1
            self.min_freq = 1


    
    def remove(self, node):

        pre = node.prev
        nex = node.next

        node.prev = None
        node.next = None
        
        nex.prev = pre

        pre.next = nex

    
    def insert(self, node, freq):

        if freq not in self.freq:
            self.freq[freq] = DLL()
        
        node.prev = None
        node.next = None
        nex = self.freq[freq].head.next
        self.freq[freq].head.next = node
        node.prev = self.freq[freq].head
        node.next = nex
        nex.prev = node
        node.freq = freq

        self.hmap[node.key] = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)