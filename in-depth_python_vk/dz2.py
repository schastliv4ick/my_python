class StackIsEmpty(Exception):
    pass


class SessionStack:
    def __init__(self):
        self._array = []

    def push(self, value):
        self._array.append(value)

    def pop(self):
        if not self._array:
            raise StackIsEmpty("Cannot pop from empty stack")
        return self._array.pop()

    def __len__(self):
        return len(self._array)

    def __str__(self):
        return f"Stack({', '.join(repr(x) for x in self._array)})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self._array})"

    def __iter__(self):
        return iter(self._array)

    def __contains__(self, value):
        return value in self._array

    def __getitem__(self, index):
        return self._array[index]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._array.clear()
        return False  # не подавляем исключения

    def __eq__(self, other):
        if not isinstance(other, SessionStack):
            return NotImplemented
        return self._array == other._array