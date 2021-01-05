#Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

#Implement the MyStack class:

#void push(int x) Pushes element x to the top of the stack.
#int pop() Removes the element on the top of the stack and returns it.
#int top() Returns the element on the top of the stack.
#boolean empty() Returns true if the stack is empty, false otherwise.
#Notes:

#You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is empty operations are valid.
#Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue), as long as you use only a queue's standard operations.


#Example 1:

#Input
#["MyStack", "push", "push", "top", "pop", "empty"]
#[[], [1], [2], [], [], []]
#Output
#[null, null, null, 2, 2, false]

#Explanation
#MyStack myStack = new MyStack();
#myStack.push(1);
#myStack.push(2);
#myStack.top(); // return 2
#myStack.pop(); // return 2
#myStack.empty(); // return False


#Constraints:

#1 <= x <= 9
#At most 100 calls will be made to push, pop, top, and empty.
#All the calls to pop and top are valid.


#Follow-up: Can you implement the stack such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer. You can use more than two queues.

from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        self._top = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        self._top = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q1) > 1:
            self._top = self.q1.popleft()
            self.q2.append(self._top)
        res = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0