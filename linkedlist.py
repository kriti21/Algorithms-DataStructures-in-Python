class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self, node_before, new_data):
        if node_before is None:
            print ("Previous node must not be None.")
            return
        new_node = Node(new_data)
        new_node.next = node_before.next
        node_before.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if (self.head is None):
            self.head = new_node
            return
        current_node = self.head
        while (current_node.next != None):
            current_node = current_node.next
        current_node.next = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data, end=' ')
            temp = temp.next
        print ()


if __name__=='__main__':
    llist = LinkedList()
    llist.append(4)
    llist.push(11)
    llist.append(3)
    llist.push(16)
    llist.insertAfter(llist.head.next.next, 19)
    print ("Created linked list is ..")
    llist.printList()