class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            self.head = Node(value, self.head)

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            new_node = Node(value, None)
            current.next = new_node

    def set_head(self, index):
        current_node = self.head
        for _ in range(index):
            if current_node is None:
                return False
            current_node = current_node.next
        self.head = current_node
        return True

    def access(self, index):
        current_node = self.head
        for _ in range(index):
            if current_node is None:
                return False
            current_node = current_node.next
        return current_node.value

    def insert(self, index, value):
        if self.head is None and index > 0:
            return False

        if index == 0:
            self.prepend(value)
            return True

        current_node = self.head
        previous_node = None
        for _ in range(index):
            if current_node is None:
                return False
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = Node(value, current_node)
        return True

    def remove(self, index):
        if self.head is None:
            return False

        current_node = self.head
        previous_node = None
        for _ in range(index):
            if current_node is None:
                return False
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return False

        previous_node.next = current_node.next
        return True

    def print(self):
        if self.head is None:
            print("list is empty")
        else:
            print("--------- DoublyLinkedList Element(head -> tail) ---------")
            current_node = self.head
            while current_node is not None:
                print(current_node.value)
                current_node = current_node.next
            print("-----------------------------------------------------------")
