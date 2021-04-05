import array


class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if self.rear == self.capacity:
            print("StackOverflow")
            return False
        self.array[self.rear] = value
        self.rear += 1
        return True

    def get(self):
        if self.front == self.rear:
            print("StackUnderflow")
            return None
        value = self.array[self.front]
        self.front += 1
        return value

    def peek(self):
        if self.front == self.rear:
            print("StackUnderflow")
            return None
        value = self.array[self.front]
        return value

    def print(self):
        if self.front == self.rear:
            print("No Element")

        values = "values: "

        if self.front == self.rear:
            values += "None"
            print(values)
            return

        for i in range(self.front, self.rear):
            values += str(self.array[i]) + " "
        print(values)


if __name__ == "__main__":
    queue = LinearQueue(5)
    queue.print()

    queue.put(1)
    queue.put(2)
    queue.put(3)
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
