import unittest

from dll import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_init_without_data(self):
        """ Тест конструктора, инициализация экземпляра без данных. """
        ll = LinkedList()

        self.assertEqual("[]", str(ll))
        self.assertEqual(0, ll._len)
        self.assertIsNone(ll._head, ll._tail)

    def test_init_with_data(self):
        """ Тест конструктора, инициализация экземпляра с данными. """
        ll = LinkedList([1, 2, 3])

        self.assertEqual("[1, 2, 3]", str(ll))
        self.assertEqual("Node(1, Node(2))", repr(ll._head))
        self.assertEqual("Node(3, None)", repr(ll._tail))
        self.assertEqual(3, ll._len)

    def test_getitem(self):
        """ Тест метода getitem, корректность работы по индексу. """
        ll = LinkedList([1, 2, 3])

        self.assertEqual(2, ll[1])

    def test_setitem(self):
        """ Тест метода setitem, корректность замены значения по индексу. """
        ll = LinkedList([1, 2, 3])
        LinkedList.__setitem__(ll, 1, '80')

        self.assertEqual('80', ll[1])
        self.assertEqual("[1, '80', 3]", str(ll))

    def test_del_head_node(self):
        """ Тест метода delitem, корректность удаления узла по индексу 0. """
        ll = LinkedList([1, 2, 3])

        del ll[0]

        self.assertEqual(2, ll._len, msg="Не правильная длина результирующего списка")
        self.assertEqual("[2, 3]", str(ll))
        self.assertEqual(2, ll._head.value)

    def test_del_body_node(self):
        """ Тест метода delitem, корректность удаления узла по индексу от 1 до Len -2. """
        ll = LinkedList([1, 2, 3])

        del ll[1]

        self.assertEqual(2, ll._len, msg="Не правильная длина результирующего списка")
        self.assertEqual("[1, 3]", str(ll))

    def test_del_tail_node(self):
        """ Тест метода delitem, корректность удаления узла по индексу len - 1. """
        ll = LinkedList([1, 2, 3])

        del ll[2]

        self.assertEqual(2, ll._len, msg="Не правильная длина результирующего списка")
        self.assertEqual("[1, 2]", str(ll))
        self.assertEqual(2, ll._tail.value)

    def test_insert_head(self):
        """ Тест метода insert, корректность вставки узла по индексу 0. """
        ll = LinkedList([1, 2, 3])

        ll.insert(0, 100)

        self.assertEqual('[100, 1, 2, 3]', str(ll))
        self.assertEqual(4, ll._len)
        self.assertEqual(100, ll._head.value)

    def test_insert_body(self):
        """ Тест метода insert, корректность вставки узла по индексу в диапазоне от 1 до len -2. """
        ll = LinkedList([1, 2, 3])

        ll.insert(1, 100)

        self.assertEqual('[1, 100, 2, 3]', str(ll))
        self.assertEqual(4, ll._len)

    def test_insert_tail(self):
        """ Тест метода insert, корректность вставки узла по индексу len - 1. """
        ll = LinkedList([1, 2, 3])

        ll.insert(2, 100)

        self.assertEqual('[1, 2, 3, 100]', str(ll))
        self.assertEqual(4, ll._len)
        self.assertEqual(100, ll._tail.value)

    def test_append(self):
        """ Тест метода append, корректность добавдения узла в конец последовательности. """
        ll = LinkedList([1, 2, 3])

        ll.append(100)

        self.assertEqual('[1, 2, 3, 100]', str(ll))
        self.assertEqual(4, ll._len)
        self.assertEqual(100, ll._tail.value)
