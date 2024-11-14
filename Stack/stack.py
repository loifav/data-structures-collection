class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        print("Element ajouté : ", value)
        self.stack.append(value)

    def pop(self):
        if not self.isEmpty():
            print("pop : ",self.stack.pop())
        else:
            print("pop : La stack est vide")

    def isEmpty(self):
        return len(self.stack) == 0

    def top(self):
        if self.isEmpty():
            print("top : La stack est vide")
        print("top : ",self.stack[-1])

if __name__ == "__main__":
    Datastack = Stack()

    Datastack.pop()
    Datastack.push(10)
    Datastack.push(20)
    Datastack.top()
    Datastack.push(30)
    print("Stack : ", Datastack.stack)
    Datastack.top()
    Datastack.pop()
    Datastack.pop()
    print("Stack : ", Datastack.stack)
    