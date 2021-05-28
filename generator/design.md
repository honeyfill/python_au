# Design

+ [Min Stack](#min-stack)
+ [Implement Queue Using Stacks](#implement-queue-using-stacks)
+ [Implement Stack Using Queues](#implement-stack-using-queues)
## Min Stack 

https://leetcode.com/problems/min-stack/

```python
class MinStack:
    def __init__(self):
        self.A = []
        self.M = []
    def push(self, x):
        self.A.append(x)
        M = self.M
        M.append( x if not M else min(x,M[-1]) )
    def pop(self):
        self.A.pop()
        self.M.pop()
    def top(self):
        return self.A[-1]
    def getMin(self):
        return self.M[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
## Implement Queue Using Stacks 

https://leetcode.com/problems/implement-queue-using-stacks/

```python
class MyQueue:
    def __init__(self):
        self.stack=[]
        self.front=0
        self.size=0

    def push(self, x: int) -> None:
        self.size+=1
        self.stack.append(x)

    def pop(self) -> int:
        self.size-=1
        self.front+=1
        return self.stack[self.front-1]

    def peek(self) -> int:
        return self.stack[self.front]

    def empty(self) -> bool:
        return self.size==0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```
## Implement Stack Using Queues 

https://leetcode.com/problems/implement-stack-using-queues/

```python
from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()


    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append( self.queue.popleft() )


    def pop(self) -> int:
        return self.queue.popleft()


    def top(self) -> int:
        return self.queue[0]


    def empty(self) -> bool:
        return (not self.queue)



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```
