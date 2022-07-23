import unittest

from dln_node import Node


class TestCase(unittest.TestCase):
    def test_init_node_without_next(self):
        """ Тест узла после инициализации с аргументом next_ по умолчанию. """
        node = Node(5)

        self.assertIsNone(node.next)
        self.assertEqual(5, node.value)

    def test_init_node_with_next(self):
        """ Тест следующего узла после инициализации с переданным аргументом next_. """
        right_node = Node('right_node')
        left_node = Node('left_node', next_=right_node)
        self.assertIs(right_node, left_node.next)
        self.assertEqual('left_node', left_node.value)

        self.assertIsNone(right_node.next)
        self.assertEqual('right_node', right_node.value)

    def test_repr_node_without_next(self):
        """ Тест метода __repr__, для случая когда нет следующего узла. """
        node = Node(5)

        expected_repr = 'Node(5, None)'
        self.assertEqual(expected_repr, repr(node))

    def test_repr_node_with_next(self):
        """ Тест метода __repr__, для случая когда установлен следующий узел. """
        node = Node(5, Node(10))

        expected_repr = 'Node(5, Node(10))'
        self.assertEqual(expected_repr, repr(node))

    def test_str(self):
        """ Тест метода __str__, корректность отображения атрибута value. """
        some_value = 5
        node = Node(some_value)

        self.assertEqual(str(some_value), str(node))
