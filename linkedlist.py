class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n


class LinkedList:

    def __init__(self, arr):
        if type(arr) == list:
            self.head = Node(arr[0], None)
            tail = self.head
            for i in range(1, len(arr)):
                temp = Node(arr[i], None)
                tail.next = temp
                tail = tail.next
        elif type(arr) == Node:
            self.head = arr


if __name__ == "__main__":
    a1 = [10, 20, 30, 40]
    h1 = LinkedList(a1)
