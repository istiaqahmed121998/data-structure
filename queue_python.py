class Error(Exception):
    pass


class ArrayQueue:
    def __init__(self, size):
        self.array_queue = [None] * size
        self.capacity = size
        self.front = self.rear = -1

    def is_empty_queue(self):
        """
        If the front of the queue is -1, then the queue is empty
        :return: The front of the queue
        """
        return self.front == -1

    def is_full_queue(self):
        """
        If the next index of the rear is the same as the front, then the queue is full
        :return: The function is_full_queue() returns True if the queue is full and False if the queue is not full.
        """
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, data):
        """
        If the queue is full, raise an error. Otherwise, increment the rear pointer and add the data to the queue. If the
        queue was empty, set the front pointer to the rear pointer

        :param data: The data to be inserted into the queue
        """
        if self.is_full_queue():
            raise Error('Queue Overflow')
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.array_queue[self.rear] = data
            if self.front == -1:
                self.front = self.rear

    def dequeue(self):
        """
        If the queue is empty, raise an error. Otherwise, return the data at the front of the queue and increment the front
        index
        :return: The data that is being returned is the data that is being removed from the queue.
        """
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
