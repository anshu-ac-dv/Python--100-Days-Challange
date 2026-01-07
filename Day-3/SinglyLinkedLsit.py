class Node: 
    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head


    def insert_at_end(self, value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp


    def insert_at_beginning(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp


    def insert_in_between(self, value, position):
        temp = Node(value)
        t1 = self.head
        while(t1.next != None):
            if(t1.data == position):
                temp.next = t1.next
                t1.next = temp
                t1 = t1.next
            t1 = t1.next

    def PrintLinkedList(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)

obj = SinglyLinkedList()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_beginning(5)
obj.insert_at_end(50)
obj.insert_in_between(25,20)
obj.PrintLinkedList()