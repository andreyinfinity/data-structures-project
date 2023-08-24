class Node:
    """Класс для узла стека"""
    nodes = []

    def __init__(self, data, next_node: object):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.nodes.append(next_node)
        self.next_node = self.nodes[-1]


class Stack:
    """Класс для стека"""
    top = None
    next_node = None

    def __init__(self):
        """Конструктор класса Stack"""

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.next_node = Node(data, self.next_node)
        self.top = self.next_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        data = self.top.data
        self.top = self.top.next_node
        return data
