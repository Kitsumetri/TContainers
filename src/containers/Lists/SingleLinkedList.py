from typing import (
    Generic, TypeVar, Iterable
)

_T = TypeVar('_T')
class Node(Generic[_T]):
    def __init__(self, value: _T, next_node=None):
        """
        :param value: Value of a node;
        :type value: _T
        :param next_node: Reference to another node;
        :type next_node: Node | None
        """
        self.__value: _T = value
        self.__next: [Node | None] = next_node

    def __str__(self, print_next: bool = False) -> str:
        return f"Node(value={self.__value}, next={self.__next})" if print_next \
            else f"Node(value={self.__value})"

    def __repr__(self, print_next: bool = False) -> str:
        return f"Node(value={self.__value}, next={self.__next})" if print_next \
            else f"Node(value={self.__value})"

    @property
    def next(self): return self.__next

    @next.setter
    def next(self, next_node) -> None: self.__next = next_node

    @property
    def value(self) -> _T: return self.__value

    @value.setter
    def value(self, value: _T) -> None: self.__value = value

class SingleLinkedList(Generic[_T]):
    """
    Linked List class with elements that is represented as Nodes

    [head] -> [head.next] -> [head.next.next] -> ... -> [tail] -> null
    """
    def __init__(self):
        self.__head = None

    def __iter__(self) -> Iterable[_T]:
        current: SingleLinkedList = self.__head
        while current:
            yield current
            current = current.next

    def __str__(self, print_next=False):
        return " -> ".join([node.__str__(print_next) for node in self]) + ' -> null'

    def push_back(self, value: _T) -> None:

        """
        :param value: Value to push into the list
        :type value: _T
        :return: None
        """

        if not self.__head:
            self.__head = Node(value)
        else:
            if not isinstance(value, type(self.__head.value)):
                raise TypeError(f"Given type: {type(value)}, "
                                f"Expected type: {type(self.__head.value)}")

            current = self.__head
            while current.next:
                current = current.next
            current.next = Node(value)

    def push_front(self, value: _T) -> None:
        if self.__head is not None and (not isinstance(value, type(self.__head.value))):
            raise TypeError(f"Given type: {type(value)}, "
                            f"Expected type: {type(self.__head.value)}")

        new_node = Node(value)
        new_node.next = self.__head
        self.__head = new_node

    def pop_back(self) -> Node:
        if self.__head is None:
            raise IndexError("pop_back() is called on an empty linked list.")

        if self.__head.next is None:
            result: Node = self.__head
            self.__head = None
        else:
            current = self.__head
            while current.next.next:
                current = current.next

            result: Node = current.next
            current.next = None
        return result

    # def pop_front(self) -> None | Node:
    #     if self.__head is None:
    #         raise IndexError("pop_front() is called on an empty linked list.")
    #     result: Node = self.__head
    #     self.__head = self.__head.next
    #     return result

    def reverse(self) -> None:
        previous = None
        current: SingleLinkedList = self.__head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.__head: SingleLinkedList = previous

    def remove(self, index: int) -> Node:
        if index < 0:
            raise IndexError('Index is a negative number.')

        if self.__head is None:
            raise IndexError('Index is out of range.')

        current_index = 0
        current = self.__head
        previous = None

        while current.next and current_index < index:
            previous = current
            current = current.next
            current_index += 1

        if current_index < index:
            raise IndexError('Index is out of range.')
        elif index == 0:
            result = self.__head
            self.__head = self.__head.next
        else:
            result = previous.next
            previous.next = current.next
        return result
