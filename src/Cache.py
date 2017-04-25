import datetime
import sys

def canEvict(value):
    return True

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    dummyValue = -1

    def __init__(self, maxSize, canEvictFunc=canEvict):
        self.maxSize = maxSize
        self.size = 0
        self.dict = {}
        self.canEvictFunc = canEvictFunc

        # head and tail always point to dummy nodes
        self.head = Node(self.dummyValue)
        self.tail = Node(self.dummyValue)
        self.head.next = self.tail
        self.tail.prev = self.head

    def full(self):
        return self.size  == self.maxSize

    def debug(self):
        node = self.head.next
        while node != self.tail:
            print(node.value)
            print() 
            node = node.next

    def get(self, key):
        if key not in self.dict:
            return None
        else:
            return self.dict[key].value

    def put(self, key, val):

        if key in self.dict:
            # id present in Cache; just update it
            node = self.dict[key]
            node.value = val

            # remove it from where it is
            node.prev.next = node.next
            node.next.prev = node.prev
            
            # reattach it at head
            node.next = self.head.next
            node.prev = self.head

            self.head.next.prev = node
            self.head.next = node

            return node.value
        else:
            # id not present
            if self.full():
                if not self.evict():
                    print("Unable to evict entry from LRUCache: try increasing maxSize?")
                    return None
            
            # insert in list
            node = Node(val, self.head, self.head.next)
            self.head.next.prev = node
            self.head.next = node
            
            self.size += 1
            self.dict[key] = node

            return node.value

    
    # Don't use this
    def remove(self, key):
        if key not in self.dict:
            return False
        else:
            node = self.dict[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
            del self.dict[key]
            return True
        

    # starting from tail 
    # go through the list until canEvictFunc says True
    def evict(self):
        node = self.tail.prev
        while node != self.head:
            if self.canEvictFunc(node.value):
                node.prev.next = node.next
                node.next.prev = node.prev
                self.size -= 1
                return True
            node = node.prev
        return False

