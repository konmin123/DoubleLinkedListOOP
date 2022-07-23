from typing import Any, Iterable, Optional, Iterator
from collections.abc import MutableSequence

from dln_node import Node
from dln_node import Dln


class LinkedList(MutableSequence):
    """ Класс описывающий связанный список. """
    CLASS_NODE = Node

    def __init__(self, data: Iterable = None):
        """ Конструктор связнного списка. """
        self._len = 0
        self._head: Optional[Node] = None
        self._tail = self._head

        if data is not None:
            for value in data:
                self.append(value)

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index):
        """ Метод удаляет узел по указанному индексу. """

        if not 0 <= index < self._len:
            raise ValueError

        if not isinstance(index, int):
            raise TypeError

        if index == 0:
            self._head = LinkedList.step_by_step_on_nodes(self, index + 1)

        elif index == self._len - 1:
            current_node = LinkedList.step_by_step_on_nodes(self, index - 1)
            current_node.next = None
            self._tail = current_node

        else:
            left_node = LinkedList.step_by_step_on_nodes(self, index - 1)
            right_node = LinkedList.step_by_step_on_nodes(self, index + 1)
            LinkedList.linked_nodes(left_node, right_node)
        self._len -= 1

    def __len__(self) -> int:
        """ Метод возвращает длину связанного списка. """
        return self._len

    def __str__(self) -> str:
        """ Метод возвращает значения последовательности в виде списка. """
        return f"{self.to_list()}"

    def __repr__(self) -> str:
        """ Метод возвращает последовательность в виде связанных нод. """
        return f"{self.__class__.__name__}({self.to_list()})"

    def insert(self, index: int, value) -> None:
        """ Метод вставляет новую ноду с заданным значением по указанному индексу. """
        insert_node = self.CLASS_NODE(value)

        if self._head is None:
            self.append(insert_node)

        elif index == 0:
            insert_node.next = self._head
            self._head = insert_node

        elif index == self._len - 1:
            self._tail.next = insert_node
            self._tail = insert_node

        else:
            left_node = LinkedList.step_by_step_on_nodes(self, index - 1)
            right_node = LinkedList.step_by_step_on_nodes(self, index)
            self.linked_nodes(left_node, insert_node)
            self.linked_nodes(insert_node, right_node)
        self._len += 1

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = self.CLASS_NODE(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Метод выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self._len:  # для for
            raise IndexError()

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """Метод, который связывает между собой два узла. """
        left_node.next = right_node

    def to_list(self) -> list:
        """ Метод формирующий список значений всех узлов односвязного списка. """
        return [linked_list_value for linked_list_value in self]

    def nodes_iterator(self) -> Iterator[Node]:
        """ Метод итерации по узлам односвязного списка. """
        current_node = self._head
        for _ in range(self._len):
            yield current_node
            current_node = current_node.next

    def clear(self):
        """ Метод удаляющий односвязаный список. """
        self._head = None
        self._tail = None

        self._len = 0


class DoubleLinkedList(LinkedList):
    """ Класс описывающий двусвязанный список. """
    CLASS_NODE = Dln

    @staticmethod
    def linked_nodes(left_node: Dln, right_node: Optional[Dln] = None) -> None:
        """ Метод, который связывает между собой два узла в двусвязанном списке."""
        left_node.next = right_node
        right_node.prev = left_node


if __name__ == "__main__":
    pass
