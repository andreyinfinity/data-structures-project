"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        self.stack = Stack()
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')
        self.assertEqual(self.stack.top.data,'data3')
        self.assertEqual(self.stack.top.next_node.data,'data2')
        self.assertEqual(self.stack.top.next_node.next_node.data,'data1')
        self.assertEqual(self.stack.top.next_node.next_node.next_node,None)
        with self.assertRaises(AttributeError):
            self.stack.top.next_node.next_node.next_node.data

    def test_pop(self):
        self.stack = Stack()
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')
        self.assertEqual(self.stack.pop(), 'data3')
        self.assertEqual(self.stack.top.data, 'data2')
        self.assertEqual(self.stack.pop(), 'data2')
        self.assertEqual(self.stack.top.data, 'data1')
        self.assertEqual(self.stack.pop(), 'data1')
        self.assertEqual(self.stack.top, None)
