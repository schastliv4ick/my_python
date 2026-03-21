class Vector:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return str((self._x, self._y))
    def __repr__(self) -> str:
        return f"Vector(x={self._x}, y={self._y})"
    
    def __add__(self, other: Any) -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(f"Can not estimate vector wiyh {type(other)}")
        return Vector(self._x + other._x, self._y + other._y)
    def __sub__(self, other: Any) -> "Vector":
        pass
    def __mul__(self, other: Any) -> "Vector":
        pass
    def __eq__(self, value: Any) -> "Vector":
        pass
