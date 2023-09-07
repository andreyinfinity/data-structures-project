class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None

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
            except TypeError:
                print("Данные не являются словарем или в словаре нет id.")
            node = node.next_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string
