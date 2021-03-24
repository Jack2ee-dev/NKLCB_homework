class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            new_node = Node(value, self.tail, None)
            self.tail.next = new_node
            self.tail = new_node
        return True

    def get(self):
        if self.head is None:
            return None

        if self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            return value

        node = self.head
        self.head = self.head.next
        self.head.prev = None
        return node.value

    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    def print(self):
        values = "values: "

        if self.head is None:
            return values + "None"

        curr = self.head
        while curr is not None:
            values += str(curr.value) + " "
            curr = curr.next
        print(values)


queue = LinkedQueue()
queue.print()

queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)
queue.put(6)
queue.print()

print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())
queue.print()

queue.put(4)
queue.put(5)
queue.put(6)
queue.print()

print(queue.get())
print(queue.get())
print(queue.get())
queue.print()
