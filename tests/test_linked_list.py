"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_insert(self):
        """
        Тест добавления элемента в очередь.
        """
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})
        self.assertEqual(self.ll.head.data, {'id': 0})
        self.assertEqual(self.ll.head.next_node.data, {'id': 1})
        self.assertEqual(self.ll.head.next_node.next_node.data, {'id': 2})
        self.assertEqual(self.ll.head.next_node.next_node.next_node.data, {'id': 3})

    def test_to_list(self):
        """
        Тест метода to_list.
        """
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(self.ll.to_list(), [{'id': 0, 'username': 'serebro'},
    {'id': 1, 'username': 'lazzy508509'},
    {'id': 2, 'username': 'mik.roz'},
    {'id': 3, 'username': 'mosh_s'}])

    def test_get_data_by_id(self):
        """
        Тест метода get_data_by_id.
        """
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(self.ll.get_data_by_id(3), {'id': 3, 'username': 'mosh_s'})

    def test_str(self):
        """Тест магического метода str."""
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})
        self.assertEqual(str(self.ll), " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")
