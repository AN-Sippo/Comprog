class ListNode:
    def __init__(self, val, key, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next


class OrderedDict:
    def __init__(self):
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.tail.prev = self.head
        self.head.next = self.tail
        self.dic = {}

    def get(self, key):
        if key in self.dic:
            self.move_to_last(key)
            return self.dic[key].val
        else:
            return -1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        self.dic[node.key] = node
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        self.tail.prev = node
        node.next = self.tail

    def set(self, key, val):
        node = ListNode(val, key)
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)
        self.add(node)

    def pop_lru(self):
        node_to_remove = self.head.next
        self.remove(node_to_remove)
        self.dic.pop(node_to_remove.key)

    def move_to_last(self, key):
        old_node = self.dic[key]
        self.remove(old_node)
        self.add(old_node)

    def __len__(self):
        return len(self.dic)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = OrderedDict()

    def get(self, key: int) -> int:
        res = self.dic.get(key)
        return res

    def put(self, key: int, value: int) -> None:
        self.dic.set(key, value)
        if len(self.dic) > self.capacity:
            self.dic.pop_lru()
