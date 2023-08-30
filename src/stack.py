class Node:
    """Класс для узла стека"""
    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""
    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        data_list = []
        node = self.top
        while node is not None:
            data = node.data
            data_list.append(data)
            node = node.next_node
        return '\n'.join(data_list)

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.top = Node(data, self.top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        data = self.top.data
        self.top = self.top.next_node
        return data
