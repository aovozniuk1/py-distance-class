from typing import Any


class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, int):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, int):
            return Distance(self.km + other)
        return NotImplemented

    def __mul__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km * other.km)
        if isinstance(other, int):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km / other.km)
        if isinstance(other, int):
            return Distance(self.km / other)
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, int):
            return self.km < other
        return NotImplemented

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, int):
            return self.km <= other
        return NotImplemented

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, int):
            return self.km > other
        return NotImplemented

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, int):
            return self.km >= other
        return NotImplemented

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, int):
            return self.km == other
        return NotImplemented
