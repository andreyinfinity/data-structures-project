class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None

    def __len__(self) -> int:
        """Возвращает количество элементов списка"""
        n = 0
        node = self.head
        if node is None:
            return n
        while node:
            n += 1
            node = node.next_node
        return n

    def __getitem__(self, index: int):
        """Возвращает данные из списка по индексу"""
        if not isinstance(index, int):
            raise TypeError('Значение индекса должно быть целым числом')
        elif index < 0:
            index += len(self)
        if index >= len(self) or index < 0:
            raise IndexError('Значение индекса не должно превышать длину списка ')
        else:
            n = 0
            node = self.head
            while n < index:
                n += 1
                node = node.next_node
            return node.data

    def __setitem__(self, index: int, data):
        """Добавляет данные в список по индексу. Если индекс отрицательный,
        то отсчет идет от конца списка."""
        if not isinstance(index, int):
            raise TypeError('Значение индекса должно быть целым числом')
        elif index < 0:
            index += len(self)
        if index > len(self) or index < 0:
            raise IndexError('Значение индекса не должно превышать длину списка')
        elif index == 0:
            self.insert_beginning(data=data)
        elif index == len(self):
            self.insert_at_end(data=data)
        else:
            n = 0
            node = self.head
            while n < index:
                n += 1
                prev_node = node
                node = node.next_node
            new_node = Node(data=data, next_node=node)
            prev_node.next_node = new_node

    def __delitem__(self, index: int):
        """Удаляет данные из списка по индексу. Если индекс отрицательный,
        то отсчет идет от конца списка."""
        if not isinstance(index, int):
            raise TypeError('Значение индекса должно быть целым числом')
        elif index < 0:
            index += len(self)
        if index > len(self) or index < 0:
            raise IndexError('Значение индекса не должно превышать длину списка')
        elif index == 0:
            self.head = self.head.next_node
        else:
            n = 0
            node = self.head
            while n < index:
                n += 1
                prev_node = node
                node = node.next_node
            prev_node.next_node = node.next_node

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        self.head = Node(data, self.head)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next_node is not None:
                node = node.next_node
            node.next_node = new_node

    def to_list(self) -> list:
        """Возвращает список с данными, находящимися в узлах списка"""
        list_nodes = []
        node = self.head
        if node is None:
            return list_nodes
        while node:
            list_nodes.append(node.data)
            node = node.next_node
        return list_nodes

    def get_data_by_id(self, id_value):
        """Возвращает первый найденный словарь с ключом 'id', значение которого равно id_value """
        node = self.head
        if node is None:
            return "Список пуст."
        while node:
            try:
                if node.data['id'] == id_value:
                    return node.data
            except TypeError as er:
                print(f"{er.__class__.__name__}: Данные не являются словарем или в словаре нет id.")
                return f"{er.__class__.__name__}: Данные не являются словарем или в словаре нет id."
            except KeyError as er:
                print(f"{er.__class__.__name__}: Данные не являются словарем или в словаре нет id.")
                return f"{er.__class__.__name__}: Данные не являются словарем или в словаре нет id."

            node = node.next_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return "Список пуст."

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string
