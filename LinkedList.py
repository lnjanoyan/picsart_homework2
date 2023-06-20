class Node:
    def __init__(self, data: str) -> None:
        self._data = data
        self._prev = None
        self._next = None


class LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self) -> bool:
        return self._head is None

    def prepend(self, data: str) -> None:
        new = Node(data)
        if self._head is None:
            self._tail = new
        new._next = self._head
        new._prev = None
        self._head = new

    def append(self, data: str) -> None:
        new = Node(data)
        if self._head is not None:
            new._prev = self._tail
            self._tail._next = new
            new._next = None
        else:
            self._head = new
            new._next = None
            new._prev = None
        self._tail = new

    def insert_after(self, target_data: str, data: str):
        current = self._head
        new = Node(data)
        while current is not None:
            if current._data == target_data:
                tmp = current._next
                current._next = new
                new._next = tmp
                if current._next is None:
                    self._tail = new
                break
            current = current._next
        else:
            print('No such data in linkedlist')

    def insert_before(self, target_data: str, data: str):
        current = self._head
        new = Node(data)
        while current is not None:
            if current._data == target_data:
                new._next = current
                new._prev = current._prev
                tmp = current._prev
                current._prev = new
                if tmp is not None:
                    tmp._next = new
                else:
                    self._head = new
                break
            current = current._next
        else:
            print('No such data in linkedlist')

    def delete(self, data: str):
        current = self._head
        while current is not None:
            if current._data == data:
                if current._next is None:
                    current._prev._next = None
                    self._tail = current._prev._next
                    del current
                    break
                elif current._prev is None:
                    current._next._prev = None
                    self._head = current._next
                    del current
                    break
                else:
                    current._prev._next = current._next
                    current._next._prev = current._prev
                    del current
                    break
            current = current._next
        else:
            print('No such data in linked lise')

    def display(self):
        current = self._head
        while current is not None:
            print(current._data, end=',')
            current = current._next


ll = LinkedList()
ll.prepend('555')
ll.append('888')
ll.append('999')
ll.display()
print('\n')
ll.insert_before('888', '777')
ll.delete('888')
ll.insert_before('555', '444')
ll.insert_after('555', '666')
ll.prepend('333')
ll.display()
