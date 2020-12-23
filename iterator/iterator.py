class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.lenght = 0
        self.counter = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.lenght:
            return -1
        if self.lenght == 0:
            return -1
        i = 0
        now = self.head
        while i != index:
            now = now.next
            i += 1
        return now.val

    def addAtHead(self, val: int) -> None:
        added = Node(val)
        self.lenght += 1
        if self.head is None:
            self.head = added
        else:
            added.next = self.head
            self.head = added

    def addAtTail(self, val: int) -> None:
        if self.lenght == 0:
            self.addAtHead(val)
        else:
            added = Node(val)
            self.lenght += 1
            now = self.head
            while now.next is not None:
                now = now.next
            now.next = added

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.lenght:
            self.addAtTail(val)
        elif index < self.lenght:
            added = Node(val)
            self.lenght += 1
            i = 1
            first = self.head
            second = first.next
            while i < index:
                first = first.next
                second = first.next
                i += 1
            first.next = added
            added.next = second

    def deleteAtIndex(self, index: int) -> None:
        if self.lenght > index >= 0:
            if index == 0:
                self.head = self.head.next
            else:
                i = 1
                first = self.head
                while i < index:
                    first = first.next
                    i += 1
                first.next = first.next.next
            self.lenght -= 1

    def __iter__(self):
        if self.counter != 0:
            self.counter = 0
        return self

    def __next__(self):
        if self.counter < self.lenght:
            self.counter += 1
            return self.get(self.counter - 1)
        else:
            raise StopIteration
