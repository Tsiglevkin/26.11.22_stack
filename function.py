from data import dict_


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        else:
            result = self.stack.pop()
            return result

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)


def check_balance(braket_string):
    stack = Stack()
    for elem in braket_string:
        if elem in dict_:
            stack.push(elem)
        elif elem == dict_.get(stack.peek()):
            stack.pop()
        else:
            return 'Несбалансировано'
    if stack.is_empty():
        return 'Сбалансировано'
