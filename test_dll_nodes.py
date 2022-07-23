import unittest

from dln_node import Dln


class TestCase(unittest.TestCase):
    def test_init_node_without_next_prev(self):
        """ Тест узла после инициализации с аргументом next_ и prev по умолчанию. """
        node = Dln(5)

        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)
        self.assertEqual(5, node.value)

    def test_init_node_with_next_prev(self):
        """ Тест узла после инициализации с переданными аргументами next_ и prev. """
        left_dln = Dln(1)
        right_dln = Dln(3)
        curren_dln = Dln(2, left_dln, right_dln)

        self.assertIs(right_dln, curren_dln.next)
        self.assertIs(left_dln, curren_dln.prev)
        self.assertEqual(2, curren_dln.value)

    def test_repr_node_without_next_prev(self):
        """ Тест метода __repr__, для случая когда нет следующего и предыдущего узла. """
        dln = Dln(5)

        expected_repr = 'Dln(5, None, None)'
        self.assertEqual(expected_repr, repr(dln))

    def test_repr_node_with_next_prev(self):
        """ Тест метода __repr__, для случая когда установлен следующий узел и предыдущий узел. """
        left_dln = Dln(1)
        right_dln = Dln(3)
        curren_dln = Dln(2, left_dln, right_dln)

        expected_repr = 'Dln(2, Dln(1), Dln(3))'
        self.assertEqual(expected_repr, repr(curren_dln))

    def test_str(self):
        """ Тест метода __str__, корректность отображения атрибута value. """
        some_value = 5
        dln = Dln(some_value)

        self.assertEqual(str(some_value), str(dln))
