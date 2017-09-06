class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


class QueueException(Exception):
    pass


class QueueEmpty(QueueException):
    pass


class Queue(object):
    def __init__(self, *items):
        self.end = None
        self.size = 0
        self.front = None
        for item in items:
            self.append(item)

    def __iter__(self):
        node = self.front
        while node:
            yield node.val
            node = node.next

    def append(self, val):
        new_node = Node(val)
        if not self.end:
            self.end = self.front = new_node
        else:
            self.end.next, self.end = new_node, new_node
        self.size += 1

    def dequeue(self):
        if not self.front:
            raise QueueEmpty()
        val = self.front.val
        self.front = self.front.next
        self.size -= 1
        return val
