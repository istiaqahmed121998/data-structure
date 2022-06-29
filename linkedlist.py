class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n


class LinkedList:

    def __init__(self, arr):
        """
        If the input is a list, then create a new linked list with the elements of the list. If the input is a node, then
        create a new linked list with the node as the head

        :param arr: This is the array that you want to convert into a linked list
        """
        if type(arr) == list:
            self.head = Node(arr[0], None)
            tail = self.head
            for i in range(1, len(arr)):
                temp = Node(arr[i], None)
                tail.next = temp
                tail = tail.next
        elif type(arr) == Node:
            self.head = arr

    def count_node(self):
        """
        We start at the head and traverse the list until we reach the curr.

        We count the number of nodes we traverse.

        We return the count
        :return: The number of nodes in the linked list.
        """
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    def print_list(self):
        """
        The function prints the elements of the linked list starting from the head
        """
        curr = self.head
        while curr is not None:
            print(curr.element, end=", ")
            curr = curr.next
        print('')

    def node_at(self, idx):
        """
        Traverse the list until you find the node at the given index.

        :param idx: The index of the node we want to find
        :return: The node at the given index.
        """
        curr = self.head
        i = 0
        while curr is not None:
            if i == idx:
                return curr
            curr = curr.next
            i += 1
        return None

    def get(self, idx):
        """
        We start at the head of the list and traverse the list until we reach the index we want

        :param idx: the index of the element to get
        :return: The element at the given index.
        """
        curr = self.head
        i = 0
        while curr is not None:
            if i == idx:
                return curr.element
            curr = curr.next
            i += 1
        return None

    def set(self, idx, elem):
        """
        If the index is valid, the element at the index is replaced with the new element and the old element is returned

        :param idx: The index of the element to be replaced
        :param elem: The element to be inserted
        :return: The element that was replaced.
        """
        curr = self.head
        i = 0
        while curr is not None:
            if i == idx:
                temp = curr.element
                curr.element = elem
                return temp
            curr = curr.next
            i += 1
        return None

    def index_of(self, elem):
        """
        We start at the head of the list, and we keep going until we find the element we're looking for, or we reach the end
        of the list

        :param elem: The element to search for in the list
        :return: The index of the element in the list.
        """
        curr = self.head
        i = 0
        while curr is not None:
            if curr.element == elem:
                return i
            curr = curr.next
            i += 1
        return -1

    def contains(self, elem):
        """
        The function iterates through the linked list and returns True if the element is found, and False if it is not.

        :param elem: the element to search for
        :return: a boolean value.
        """
        curr = self.head
        i = 0
        while curr is not None:
            if curr.element == elem:
                return True

            curr = curr.next
            i += 1
        return False

    def insert(self, elem, pos):
        """
        If the position is valid, create a new node, and if the position is 0, set the new node's next to the head, and set
        the head to the new node, otherwise, iterate through the list until you reach the position, and set the new node's
        next to the current node, and set the previous node's next to the new node

        :param elem: The element to be inserted
        :param pos: The position where the new node is to be inserted
        :return: the number of nodes in the linked list.
        """
        if 0 <= pos <= self.count_node():
            new_node = Node(elem, None)
            if pos == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                count = 0
                curr = self.head
                tail = None
                while curr is not None and count < pos:
                    count += 1
                    tail = curr
                    curr = curr.next
                tail.next = new_node
                new_node.next = curr
        else:
            print('Invalid Index')
            return

    def delete(self, pos):
        """
        If the position is valid, then we traverse the list until we reach the position, and then we delete the node at that
        position

        :param pos: The position of the node to be deleted
        :return: The value of the node at the given position.
        """
        if 0 <= pos < self.count_node():
            if pos == 0:
                self.head = self.head.next
            else:
                curr = self.head
                count = 0
                while curr is not None and count < pos:
                    count += 1
                    tail = curr
                    curr = curr.next
                tail.next = curr.next
        else:
            print('Invalid Index')
            return

    def reverse(self):
        """
        We are reversing the pointer direction of each node in the linked list
        """
        curr = self.head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def rotate_left(self, k):
        """
        We find the kth node from the end of the linked list, and then we set the next of the kth node to None, and then we
        set the next of the last node to the head of the linked list

        :param k: the number of times we want to rotate the list
        """
        mod = k % 4
        curr = self.head
        tail = self.head
        count = 0
        if mod != 0:
            while tail.next is not None:
                count += 1
                if count < mod:
                    curr = curr.next
                tail = tail.next
            kthhead = curr.next
            curr.next = None
            tail.next = self.head
            self.head = kthhead

    def rotate_right(self, k):
        """
        We find the kth node from the end of the linked list, and then we make the next node of the kth node the new head of
        the linked list

        :param k: the number of times you want to rotate the linked list
        """
        mod = k % 4
        curr = self.head
        tail = self.head
        count = 0
        if mod != 0:
            while tail.next is not None:
                count += 1
                if count < self.count_node() - mod:
                    curr = curr.next
                tail = tail.next
            kthhead = curr.next
            curr.next = None
            tail.next = self.head
            self.head = kthhead


class CLinkedList:
    def __init__(self, arr):
        """
        If the input is a list, then create a new linked list with the elements of the list. If the input is a node, then
        create a new linked list with the node as the head

        :param arr: This is the array that you want to convert into a linked list
        """
        if type(arr) == list:
            self.head = Node(arr[0], None)
            tail = self.head
            for i in range(1, len(arr)):
                temp = Node(arr[i], None)
                tail.next = temp
                tail = tail.next
            tail.next = self.head
        elif type(arr) == Node:
            self.head = arr

    def count_node(self):
        curr = self.head
        count = 0
        if self.head is None:
            return count
        while True:
            curr = curr.next
            count += 1
            if curr == self.head:
                break
        return count

    def print_list(self):
        curr = self.head
        if self.head is None:
            return
        while True:
            print(curr.element, end=", ")
            curr = curr.next
            if curr == self.head:
                break
        print('')

    def insert(self, elem, pos):
        """
        If the position is valid, create a new node, and if the position is 0, set the new node's next to the head, and set
        the head to the new node, otherwise, iterate through the list until you reach the position, and set the new node's
        next to the current node, and set the previous node's next to the new node

        :param elem: The element to be inserted
        :param pos: The position where the new node is to be inserted
        :return: The new node is being returned.
        """
        if 0 <= pos <= self.count_node():
            new_node = Node(elem, None)
            if pos == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                count = 0
                curr = self.head
                tail = None
                while curr is not None and count < pos:
                    count += 1
                    tail = curr
                    curr = curr.next
                tail.next = new_node
                new_node.next = curr
        else:
            print('Invalid Index')
            return

    def delete(self, pos):
        """
        We start at the head, and traverse the list until we reach the node at the position we want to delete.

        We then set the previous node's next pointer to the node after the one we want to delete.

        We then delete the node we want to delete.

        :param pos: The position of the node to be deleted
        :return: the value of the node at the given position.
        """
        if 0 <= pos < self.count_node():
            if pos == 0:
                curr = self.head
                while curr.next != self.head:
                    curr = curr.next
                curr.next = self.head.next
                self.head = self.head.next
            else:
                curr = self.head
                count = 0
                while curr is not None and count < pos:
                    count += 1
                    tail = curr
                    curr = curr.next
                tail.next = curr.next
        else:
            print('Invalid Index')
            return


if __name__ == "__main__":
    a1 = [10, 20, 30, 40, 50, 60]
    h1 = CLinkedList(a1)
    h1.insert(70, 6)
    h1.print_list()
    h1.delete(6)
    h1.print_list()
