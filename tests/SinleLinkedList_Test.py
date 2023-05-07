import unittest

from src.containers.Lists.SingleLinkedList import (
    SingleLinkedList, Node
)

class SingleLinkedListTests(unittest.TestCase):
    def test_push_back(self):
        lst = SingleLinkedList()
        lst.push_back(1)
        lst.push_back(2)
        lst.push_back(3)
        self.assertEqual(str(lst), "Node(value=1) -> Node(value=2) -> Node(value=3) -> null")

    def test_push_back_type_error(self):
        lst = SingleLinkedList()
        lst.push_back(1)
        self.assertRaises(TypeError, lst.push_back, "2")

    def test_pop_back(self):
        lst = SingleLinkedList()
        lst.push_back(1)
        lst.push_back(2)
        lst.push_back(3)
        lst.pop_back()
        self.assertEqual(str(lst), "Node(value=1) -> Node(value=2) -> null")

    def test_pop_back_empty_list(self):
        lst = SingleLinkedList()
        self.assertRaises(IndexError, lst.pop_back)

    def test_remove(self):
        lst = SingleLinkedList()
        lst.push_back(1)
        lst.push_back(2)
        lst.push_back(3)
        lst.remove(1)
        self.assertEqual(str(lst), "Node(value=1) -> Node(value=3) -> null")

    def test_str_no_print_next(self):
        lst = SingleLinkedList()
        lst.push_back(1)
        lst.push_back(2)
        lst.push_back(3)
        self.assertEqual(lst.__str__(), "Node(value=1) -> Node(value=2) -> Node(value=3) -> null")

    def test_remove_index_out_of_range(self):
        lst = SingleLinkedList()
        lst.push_back(1)
        lst.push_back(2)
        self.assertRaises(IndexError, lst.remove, 2)

    def test_str_print_next(self):
        lst = SingleLinkedList()
        lst.push_back(1)
        lst.push_back(2)
        lst.push_back(3)
        self.assertEqual(lst.__str__(print_next=True),
                         'Node(value=1, next=Node(value=2)) -> Node(value=2, next=Node(value=3)) -> Node(value=3, next=None) -> null')

    def test_remove_at_negative_index(self):
        lst = SingleLinkedList()
        lst.push_back(1)
        lst.push_back(2)
        self.assertRaises(IndexError, lst.remove, -1)


class TestNode(unittest.TestCase):
    def test_node_creation(self):
        n = Node(5)
        self.assertEqual(n.value, 5)
        self.assertIsNone(n.next)

    def test_node_str_method(self):
        n = Node(5)
        self.assertEqual(n.__str__(print_next=False), "Node(value=5)")
        n.next = Node(6)
        self.assertEqual(n.__str__(print_next=True), "Node(value=5, next=Node(value=6))")

    def test_node_repr_method(self):
        n = Node(5)
        self.assertEqual(n.__repr__(print_next=False), "Node(value=5)")
        n.next = Node(6)
        self.assertEqual(n.__repr__(print_next=True), "Node(value=5, next=Node(value=6))")

    def test_node_next_property(self):
        n1 = Node(5)
        n2 = Node(6)
        n1.next = n2
        self.assertEqual(n1.next, n2)

    def test_node_value_property(self):
        n = Node(5)
        self.assertEqual(n.value, 5)
        n.value = 6
        self.assertEqual(n.value, 6)


if __name__ == '__main__':
    unittest.main()
