"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_insert(self):
        """
        Тест добавления элемента в список.
        """
        self.ll = LinkedList()
        # Добавление в начало пустого списка
        self.ll.insert_beginning({'id': 1})
        # Добавление в конец списка
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        # Добавление в начало списка
        self.ll.insert_beginning({'id': 0})
        # Проверка данных списка начиная с начала
        self.assertEqual(self.ll.head.data, {'id': 0})
        self.assertEqual(self.ll.head.next_node.data, {'id': 1})
        self.assertEqual(self.ll.head.next_node.next_node.data, {'id': 2})
        self.assertEqual(self.ll.head.next_node.next_node.next_node.data, {'id': 3})
        self.ll = LinkedList()
        # Добавление в конец пустого списка
        self.ll.insert_at_end({'id': 0})
        self.assertEqual(self.ll.head.data, {'id': 0})

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
        # Тест метода, когда список пуст
        self.ll = LinkedList()
        self.assertEqual(self.ll.to_list(), [])

    def test_get_data_by_id(self):
        """
        Тест метода get_data_by_id.
        """
        # Тест нормального поведения
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(self.ll.get_data_by_id(3), {'id': 3, 'username': 'mosh_s'})
        # Тест при пустом списке
        self.ll = LinkedList()
        self.assertEqual(self.ll.get_data_by_id(3), "Список пуст.")
        # Тест с неправильным key name в словаре
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'bad_id': 3, 'username': 'mosh_s'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(self.ll.get_data_by_id(3),
                         "KeyError: Данные не являются словарем или в словаре нет id.")
        # Тест с неправильным key type в словаре
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end(['bad_id'])
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(self.ll.get_data_by_id(3),
                         "TypeError: Данные не являются словарем или в словаре нет id.")

    def test_str(self):
        """Тест магического метода str."""
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})
        self.assertEqual(str(self.ll), " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")
        # Тест с пустым списком
        self.ll = LinkedList()
        self.assertEqual(str(self.ll), "Список пуст.")

    def test_len(self):
        """Тест магического метода str."""
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})
        self.assertEqual(len(self.ll), 4)
        # Тест с пустым списком
        self.ll = LinkedList()
        self.assertEqual(len(self.ll), 0)

    def test_getitem(self):
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})
        self.assertEqual(self.ll[0], {'id': 0})
        self.assertEqual(self.ll[1], {'id': 1})
        self.assertEqual(self.ll[2], {'id': 2})
        self.assertEqual(self.ll[3], {'id': 3})
        self.assertEqual(self.ll[-1], {'id': 3})
        self.assertEqual(self.ll[-2], {'id': 2})
        self.assertEqual(self.ll[-3], {'id': 1})
        self.assertEqual(self.ll[-4], {'id': 0})
        with self.assertRaises(IndexError):
            self.ll[4]
        with self.assertRaises(TypeError):
            self.ll['3']

    def test_setitem(self):
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_beginning({'id': 0})
        self.ll[1] = {'new': 1}
        self.assertEqual(self.ll[0], {'id': 0})
        self.assertEqual(self.ll[1], {'new': 1})
        self.assertEqual(self.ll[2], {'id': 1})
        self.assertEqual(self.ll[3], {'id': 2})
        with self.assertRaises(IndexError):
            self.ll[5] = {'new': 1}
        with self.assertRaises(TypeError):
            self.ll['3'] = {'new': 1}

    def test_delitem(self):
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})
        self.assertEqual(self.ll.to_list(), [{'id': 0}, {'id': 1}, {'id': 2}, {'id': 3}])
        del self.ll[2]
        self.assertEqual(self.ll.to_list(), [{'id': 0}, {'id': 1}, {'id': 3}])
        del self.ll[0]
        self.assertEqual(self.ll.to_list(), [{'id': 1}, {'id': 3}])
        del self.ll[1]
        self.assertEqual(self.ll.to_list(), [{'id': 1}])
        with self.assertRaises(IndexError):
            del self.ll[4]
        with self.assertRaises(TypeError):
            del self.ll['3']

