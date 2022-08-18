class Error(Exception):
    pass


class ArrayQueue:
    def __init__(self, size):
        self.array_queue = [None] * size
        self.capacity = size
        self.front = self.rear = -1

    def is_empty_queue(self):
        return self.front == -1

    def is_full_queue(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, data):
        if self.is_full_queue():
            raise Error('Queue Overflow')
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.array_queue[self.rear] = data
            if self.front == -1:
                self.front = self.rear

    def dequeue(self):
        if self.is_empty_queue():
            raise Error('Queue is empty')
        else:
            data = self.array_queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.capacity
            return data


if __name__ == "__main__":
    array_queue = ArrayQueue(10)
    print(array_queue.dequeue())
