'''Implementation of stack using list'''

class MyStack:

    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        if not self.arr:
            return -1
        else :
            return self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]     

    def empty(self) -> bool:
        return not self.arr 