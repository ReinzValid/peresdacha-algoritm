class Node:
    def __init__(self, value, next_node=None):
        self.value, self.next = value, next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, value):
        self.head = Node(value, self.head)

    def add_last(self, value):
        if self.head is None:
            return self.add_first(value)
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def add_after(self, target, value):
        """Добавление по значению: после первого узла со значением target."""
        current = self.head
        while current and current.value != target:
            current = current.next
        if current is None:
            return False
        current.next = Node(value, current.next)
        return True

    def remove_first(self):
        if self.head is None:
            return False
        self.head = self.head.next
        return True

    def remove_last(self):
        if self.head is None or self.head.next is None:
            return self.remove_first()
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        return True

    def remove_value(self, value):
        if self.head is None or self.head.value == value:
            return self.remove_first()
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next is None:
            return False
        current.next = current.next.next
        return True

    def show(self):
        values, current = [], self.head
        while current:
            values.append(str(current.value))
            current = current.next
        print(' -> '.join(values) if values else '(пустой список)')


if __name__ == '__main__':
    linked = LinkedList()
    for operation, args in (
        (linked.add_first, (20,)), (linked.add_first, (10,)),
        (linked.add_last, (30,)), (linked.add_after, (20, 25)),
        (linked.remove_first, ()), (linked.remove_last, ()),
        (linked.remove_value, (25,)),
    ):
        operation(*args)
        print(f'{operation.__name__}{args}:', end=' ')
        linked.show()
