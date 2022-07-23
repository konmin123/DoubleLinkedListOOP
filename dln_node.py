from typing import Any, Optional
import weakref


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """ Конструктор узла для односвязного списка. """
        self.value = value
        self.next = next_

    @property
    def next(self):
        """ Свойство для установки атрибута next. """
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        """ Сеттер для безопасного изменения значения атрибута next. """
        self.is_valid(next_)
        self._next = next_

    def __repr__(self) -> str:
        """ Метод изменяющий представление ноды односвязного списка. """
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        """ Метод изменяющий строковое отображение ноды. """
        return str(self.value)

    @classmethod
    def is_valid(cls, node: Any) -> None:
        """ Метод проверяющий, что данные являются нодой. """
        if not isinstance(node, (type(None), cls)):
            raise TypeError


class Dln(Node):
    """Класс, который описывает узел двусвязанного списка."""
    def __init__(self, value: Any, prev: Optional["Dln"] = None, next_: Optional["Dln"] = None):
        """ Конструктор узла для двусвязного списка. """
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self):
        """ Свойство для установки атрибута prev. """
        return None if self._prev is None else self._prev()

    @prev.setter
    def prev(self, prev: Optional["Node"]):
        """ Сеттер для безопасного изменения значения атрибута prev. """
        self.is_valid(prev)
        self._prev = None if prev is None else weakref.ref(prev)

    def __repr__(self) -> str:
        """ Метод изменяющий представление ноды двусвязного списка. """
        next_ = None if self.next is None else f"Dln({repr(self.next.value)})"
        prev = None if self.prev is None else f"Dln({repr(self.prev.value)})"
        return f"Dln({repr(self.value)}, {prev}, {next_})"
