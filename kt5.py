from collections import deque


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not self.items


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return not self.items


def check_brackets(s):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.push(char)
        elif char in pairs and (stack.is_empty() or stack.pop() != pairs[char]):
            return False
    return stack.is_empty()  # Остальные символы игнорируются.


if __name__ == '__main__':
    stack = Stack()
    print('Стек пуст:', stack.is_empty())
    stack.push(10)
    stack.push(20)
    print('Вершина:', stack.peek(), 'Извлечено:', stack.pop())
    queue = Queue()
    print('Очередь пуста:', queue.is_empty())
    queue.enqueue(10)
    queue.enqueue(20)
    print('Первым из очереди:', queue.dequeue())
    for text in ('( [ ] { } )', '( [ ) ]', '(()', ')(', '', 'a * (b + c)'):
        print(repr(text), '->', check_brackets(text))
