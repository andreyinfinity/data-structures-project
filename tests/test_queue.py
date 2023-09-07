"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        """
        Тест добавления элемента в очередь.
        """
        self.queue = Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual(self.queue.head.data,'data1')
        self.assertEqual(self.queue.head.next_node.data,'data2')
        self.assertEqual(self.queue.head.next_node.next_node.data,'data3')
        self.assertEqual(self.queue.tail.data,'data3')
        self.assertEqual(self.queue.tail.next_node,None)
        with self.assertRaises(AttributeError):
            self.queue.tail.next_node.data

    def test_dequeue(self):
        """
        Тест удаления элементов из стека.
        """
        self.queue = Queue()
        self.assertEqual(self.queue.dequeue(), None)
        self.assertEqual(self.queue.head, None)
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual(self.queue.dequeue(), 'data1')
        self.assertEqual(self.queue.head.data, 'data2')
        self.assertEqual(self.queue.dequeue(), 'data2')
        self.assertEqual(self.queue.head.data, 'data3')
        self.assertEqual(self.queue.dequeue(), 'data3')
        self.assertEqual(self.queue.head, None)

    def test_str(self):
        """Тест магического метода str."""
        self.assertEqual(str(Queue()), "")
        self.queue = Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual(str(self.queue), "data1\ndata2\ndata3")
