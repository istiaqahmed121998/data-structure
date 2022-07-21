class DNode:
    def __init__(self, prev, elem, next):
        self.prev = prev
        self.element = elem
        self.next = next


class DoublyLinkedList:
    def __init__(self, arr):
        """
        If the input is a list, then we create a doubly linked list with the first element of the list as the head and the
        last element of the list as the tail.

        If the input is a DNode, then we create a doubly linked list with the input as the head and the tail.

        :param arr: This is the array that you want to convert into a doubly linked list
        """
        if type(arr) == list:
            self.head = DNode(None, arr[0], None)
            self.tail = self.head
            for i in range(1, len(arr)):
                temp = DNode(None, arr[i], None)
                self.tail.next = temp
                temp.prev = self.tail
                self.tail = self.tail.next
        elif type(arr) == DNode:
            self.head = arr

    def count_node(self):
        """
        We start at the head of the linked list and traverse the list until we reach the end.

        We increment a counter variable each time we traverse a node.

        When we reach the end of the list, we return the counter variable.
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
        The function starts at the head of the list and prints each element until it reaches the end of the list
        """
        curr = self.head
        while curr is not None:
            print(curr.element, end=", ")
            curr = curr.next
        print('')

    def reverse_print(self):
        """
        We are reversing the pointer direction of each node in the linked list
        """
        tail = self.tail
        while tail is not None:
            print(tail.element, end=", ")
            tail = tail.prev
        print('')

    def insert(self, elem, pos):
        """
        We create a new node, and then we traverse the list until we find the node that is before the position we want to
        insert the new node.

        We then set the new node's next to the node that was at the position we want to insert, and we set the new node's
        previous to the node that was before the position we want to insert.

        We then set the node that was before the position we want to insert's next to the new node, and we set the node that
        was at the position we want to insert's previous to the new node.

        If the position we want to insert is the last position, we don't have to set the node that was at the position we
        want to insert's previous to the new node.

        If the position we want to insert is the first position, we don't have to set the node that was before the position
        we want to insert's next to the new node

        :param elem: The element to be inserted
        :param pos: The position where the new node is to be inserted
        :return: the number of nodes in the linked list.
        """
        if 0 <= pos <= self.count_node():
            new_node = DNode(None, elem, None)
            if pos == 0:
                new_node.next = self.head
                self.head.prev = new_node
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
                new_node.prev = tail
                new_node.next = curr
                if pos != self.count_node() - 1:
                    curr.prev = new_node
        else:
            print('Invalid Index')
            return

    def delete(self, pos):
        """
        If the position is valid, then we delete the node at that position

        :param pos: The position of the node to be deleted
        :return: the number of nodes in the linked list.
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
                if pos != self.count_node():
                    curr.next.prev = tail
        else:
            print('Invalid Index')
            return


class CDoublyLinkedList:

    def __init__(self, arr):
        """
        If the input is a DNode, then the head of the DLL is the input. If the input is a list, then the head of the DLL is
        the first element of the list, and the tail of the DLL is the last element of the list

        :param arr: The array that you want to convert to a circular doubly linked list
        """
        if type(arr) is DNode:
            self.head = arr
        elif type(arr) == list:
            self.head = DNode(None, arr[0], None)
            self.tail = self.head
            for i in range(1, len(arr)):
                temp = DNode(None, arr[i], None)
                self.tail.next = temp
                temp.prev = self.tail
                self.tail = self.tail.next
            self.tail.next = self.head
            self.head.prev = self.tail

    def count_node(self):
        curr = self.head
        count = 1
        while curr.next != self.head:
            count += 1
            curr = curr.next
        return count

    def print_list(self):
        curr = self.head
        while curr.next != self.head:
            print(curr.element, end=',')
            curr = curr.next
        print(curr.element, end='')

    def insert(self, elem, pos):
        if 0 <= pos <= self.count_node():
            new_node = DNode(None, elem, None)
            if pos == 0:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                self.head.prev = self.tail
                self.tail.next = self.head
            else:
                count = 1
                curr = self.head
                while curr.next is not self.head and count < pos:
                    count += 1
                    curr = curr.next
                tail = curr
                curr = curr.next
                tail.next = new_node
                new_node.prev = tail
                new_node.next = curr
                curr.prev = new_node
        else:
            print('Invalid Index')
            return

    def reverse_print(self):
        """
        We are reversing the pointer direction of each node in the linked list
        """
        tail = self.tail
        while tail.prev is not self.tail:
            print(tail.element, end=", ")
            tail = tail.prev
        print(tail.element, end='')
        print('')


if __name__ == "__main__":
    a1 = [10, 20, 30, 40]
    h1 = CDoublyLinkedList(a1)
    print(h1.count_node())
    h1.insert(0, 4)
    h1.reverse_print()
    # # h1.print_list()
    # h1.insert(0, 6)
    # h1.print_list()
