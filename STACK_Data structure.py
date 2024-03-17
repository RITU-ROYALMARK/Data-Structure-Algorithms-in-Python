# Stack Data Structure
'''
There are some basic operations that allow us to perform different actions on a stack.

1). Push: Add an element to the top of a stack
2). Pop: Remove an element from the top of a stack
3). IsEmpty: Check if the stack is empty
4). IsFull: Check if the stack is full
5). Peek: Get the value of the top element without removing it

'''

class stack_data:
    def __init__(self):
        self.stack = []

    def push(self,val):
        if val is None:
            return
        else:
            self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def IsEmpty(self):
        if len(self.stack) == 0:
            return "IS EMPTY"
        return "IS NOT EMPTY"

    def IsFull(self):
        if len(self.stack) >= 1:
            return "IS FULL"
        return "IS NOT FULL"

    def peek(self,index):
        if len(self.stack) > index >= 1:
            return self.stack[index]
        else:
            self.IsEmpty()
    def view(self):
        return self.stack

def pusk_auto():
    stacks = stack_data()
    for i in range(1,100,8):
        stacks.push(i)
    return stacks

stacks = pusk_auto()
print(f"VIEW :{stacks.view()}")
print(f"POP : {stacks.pop()}")
print(f"VIEW: {stacks.view()}")
print(f"IS EMPTY: {stacks.IsEmpty()}")
print(f"IS FULL: {stacks.IsFull()} ")
print(f"PEEK: {stacks.peek(1)}")



