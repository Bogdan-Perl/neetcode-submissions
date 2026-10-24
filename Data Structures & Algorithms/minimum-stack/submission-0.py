class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

        

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            # If the popped value is the current minimum, pop it from the min_stack as well
            if val == self.min_stack[-1]:
                self.min_stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1  # In case the stack is empty, return an error value

        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return -1  # In case the min_stack is empty, return an error value
        
