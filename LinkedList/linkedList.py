

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data) 

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node

    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current is not None and current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
            

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("End List")

if __name__ == "__main__":
    ll = LinkedList()
    print("Append method")
    ll.append(10)
    ll.append(50)
    ll.append(30)
    ll.append(40)
    ll.display()
    print("Delete Value: 30")
    ll.delete(30)
    ll.display()