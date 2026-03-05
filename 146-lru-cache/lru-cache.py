class Node:
    def __init__(self, key=0, value=0):
        # initialize a new node with a key, value, and prev/next pointers
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}  
        self.head = Node() 
        self.tail = Node()  
        self.capacity = capacity  
        self.size = 0  
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.add_to_head(node)
          
            self.size += 1
            if self.size > self.capacity:
                removed_node = self.remove_tail()
                del self.cache[removed_node.key]
                self.size -= 1

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_tail(self):
        
        node = self.tail.prev
        self.remove_node(node)
        return node