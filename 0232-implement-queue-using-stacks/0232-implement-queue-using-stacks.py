class MyQueue:

    def __init__(self):
        self.queue = []
        self.head = 0

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        res = self.queue[self.head]
        self.head += 1
        return res

    def peek(self) -> int:
        return self.queue[self.head]

    def empty(self) -> bool:
        return self.head == len(self.queue)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()