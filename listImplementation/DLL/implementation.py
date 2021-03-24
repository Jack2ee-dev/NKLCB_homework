class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            node = Node(value, self.head, None)
            self.head.prev = node
            self.head = node

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            new_node = Node(value, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node

    def set_head(self, index):
        if self.head is None and index > 0:
            return False
        if index == 0:
            return True

        current_node = self.head
        for _ in range(index):
            if current_node is None:
                return False
            current_node = current_node.next

        self.head = current_node
        self.head.prev = None
        return True

    def access(self, index):
        if self.head is None:
            return False
        if index == 0:
            return self.head.value

        current_node = self.head
        for _ in range(index):
            if current_node is None:
                return False
            current_node = current_node.next

        if current_node is None:
            return False

        return current_node.value

    def insert(self, index, value):
        if self.head is None and index > 0:
            return False

        if index == 0:
            self.prepend(value)

        current_node = self.head
        for _ in range(index):
            if current_node is None:
                return False
            current_node = current_node.next

        if current_node is None:
            node = Node(value, None, self.tail)
            self.tail.next = node
            self.tail = node
        else:
            node = Node(value, current_node, current_node.prev)
            current_node.prev.next = node
            current_node.next.prev = node
        return True

    def remove(self, index):
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            if self.head.prev is not None:
                self.head.prev = None

        current_node = self.head
        for _ in range(index):
            if current_node is None:
                return False
            current_node = current_node.next

        if current_node is None:
            return False
        else:
            current_node.prev.next = current_node.next
            if current_node.next is not None:
                current_node.next.prev = current_node.prev
            else:
                self.tail = current_node.prev
            return True

    def print(self):
        if self.head is None:
            print("list is empty")
        else:
            print("--------- DoublyLinkedList Element(head -> tail) ---------")
            curr = self.head
            while curr.next is not None:
                print(curr.value)
                curr = curr.next
            print("-----------------------------------------------------------")

    def printInverse(self):
        if self.head is None:
            print("list is empty")
        else:
            print("--------- DoublyLinkedList Element(tail -> head) ---------")
            curr = self.tail
            while curr.prev is not None:
                print(curr.value)
                curr = curr.prev
            print("-----------------------------------------------------------")
