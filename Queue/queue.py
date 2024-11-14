class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        print("Element ajouter : ",value)
        self.queue.append(value)

    def isEmpty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if self.isEmpty():
            print("dequeue : Queue est vide")
        print("dequeue : ", self.queue.pop(0))

    def front(self):
        print("front : ", self.queue[0])
    
    def rear(self):
        print("rear : ", self.queue[len(self.queue)-1])


if __name__ == "__main__":
    Dataqueue = Queue()

    Dataqueue.enqueue(1)
    Dataqueue.enqueue(2)
    Dataqueue.enqueue(3)
    print("Queue : ", Dataqueue.queue)
    Dataqueue.front()
    Dataqueue.dequeue()
    print("Queue : ", Dataqueue.queue)
    Dataqueue.front()
    Dataqueue.enqueue(4)
    print("Queue : ", Dataqueue.queue)
    Dataqueue.rear()
    print("Queue : ", Dataqueue.queue)


    
    