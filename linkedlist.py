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
        tail = self.head
        i = 0
        while tail is not None:
            if tail.element == elem:
                return True
            tail = tail.next
            i += 1
        return False

if __name__ == "__main__":
    a1 = [10, 20, 30, 40]
    h1 = LinkedList(a1)
