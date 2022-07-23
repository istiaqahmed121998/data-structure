class Error(Exception):
    pass


class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class ArrayStack:
    def __init__(self):

        self.top = -1
        self.capacity = 10
        self.array = [None] * 10

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, data):
        if self.is_full():
            raise Error("size is full")
        else:
            self.top += 1
            self.array.insert(self.top, data)

    def pop(self):
        if self.is_empty():
            raise Error("size is empty")
        else:
            temp = self.array[self.top]
            self.top -= 1
            return temp


class ListStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        temp = ListNode(data, self.top)
        self.top = temp

    def pop(self):
        if self.is_empty():
            raise Error("size is empty")
        else:
            data=self.top.data
            self.top=self.top.next
            return data


a = ListStack()
a.push(1)
a.push(12)
a.push(13)
print(a.pop())
