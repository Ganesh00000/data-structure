class Stack:
    stack=[]
    def push(self,n):
        self.stack.append(n)
    def pop(self):
        del self.stack[-1]
    def show(self):
        print(self.stack)

class Queue(Stack):
    def pop(self):
        del self.stack[0]



