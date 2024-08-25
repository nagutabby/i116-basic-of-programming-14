from __future__ import annotations

class Stack():
    def push(self, e: int) -> None | NeStack:
        pass
    def pop(self) -> None | EmptyStack | NeStack:
        pass
    def top(self) -> None | int:
        pass
    def __str__(self) -> str:
        return ''
    def is_empty(self):
        pass
    def is_empty_or_one(self):
        pass

class EmptyStack(Stack):
    def push(self, e: int) -> NeStack:
        return NeStack(e, self)
    def pop(self) -> EmptyStack:
        return self
    def top(self) -> None:
        return None
    def __str__(self):
        return 'empty stack'
    def is_empty(self) -> bool:
        return True
    def is_empty_or_one(self) -> bool:
        return True

class NeStack(Stack):
    def __init__(self, t: int, b: EmptyStack | NeStack) -> None:
        self.top_elt = t
        self.bottom = b
    def push(self, e: int) -> NeStack:
        return NeStack(e, self)
    def pop(self) -> EmptyStack | NeStack:
        return self.bottom
    def top(self) -> int:
        return self.top_elt
    def __str__(self) -> str:
        return f'{self.top_elt} ; {self.bottom}'
    def is_empty(self) -> bool:
        return False
    def is_empty_or_one(self) -> bool:
        return self.bottom.is_empty()
