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
            data = self.top.data
            self.top = self.top.next
            return data

    def peek(self):
        if self.is_empty():
            return -1
        else:
            data = self.top.data
            return data


class Conversion:

    def __init__(self):
        self.stack = ListStack()
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.stack.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    def infix_to_postfix(self, exp):
        """
        If the character is an operand, add it to the output. If the character is a left parenthesis, push it onto the
        stack. If the character is a right parenthesis, pop the stack and add each operator to the output until you see a
        left parenthesis. Discard the pair of parentheses. If the character is an operator, *, /, +, or -, push it onto the
        stack. However, first remove any operators already on the stack that have higher or equal precedence and add them to
        the output

        :param exp: The expression to be converted
        :return: The output is the postfix expression.
        """
        output = ''
        for i in exp:
            if i.isalpha():
                output += i

            elif i == '(':
                self.stack.push(i)

            elif i == ')':
                while self.stack.peek() != '(':
                    a = self.stack.pop()
                    output += a
                self.stack.pop()

            else:
                while not self.stack.is_empty() and self.notGreater(i):
                    output += self.stack.pop()
                self.stack.push(i)
        while not self.stack.is_empty():
            output += self.stack.pop()

        return output


a = Conversion()
print(a.infix_to_postfix('A+B-(C+D)+E'))
