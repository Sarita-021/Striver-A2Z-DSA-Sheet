# Write a program to implement stack using queue

class MyQueue:

    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        if not self.arr:
            return -1
        else:
            return self.arr.pop(0)

    # Returns the element at the front(leftmost) of the queue.
    def peek(self) -> int:
        return self.arr[0]

    def empty(self) -> bool:
        return not self.arr
    

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()