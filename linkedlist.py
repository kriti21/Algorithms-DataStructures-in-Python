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

    def size(self):
        current_node = self.head
        count = 0
        while (current_node != None):
            count += 1
            current_node = current_node.next
        return count

    def isEmpty(self):
        if (self.head is None):
            return True
        else:
            return False

    def valueAt(self, index):
        current_node = self.head
        i = 0
        while (i<index and current_node):
            current_node = current_node.next
            i += 1
        return current_node.data 

    def popFront(self):
        current_node = self.head
        item = current_node.data
        self.head = current_node.next
        return item

    def popBack(self):
        current_node = self.head
        prev_node = None
        while (current_node.next is not None):
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = None
        return current_node.data

    def front(self):
        if (self.head is None):
            print ("Empty linked list")
            return
        return self.head.data

    def back(self):
        current_node = self.head
        while (current_node.next is not None):
            current_node = current_node.next
        return current_node.data


    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data, end=' ')
            temp = temp.next
        print ()


if __name__=='__main__':
    llist = LinkedList()
    print ("Is the linked list empty .. ", end='')
    print (llist.isEmpty())
    llist.append(4)
    llist.push(11)
    llist.append(3)
    llist.push(16)
    llist.insertAfter(llist.head.next.next, 19)
    print ("Created linked list is ..")
    llist.printList()
    k = llist.size()
    print ("Size of the linked list is : ", end='')
    print (k)
    print ("Is the linked list empty .. ", end='')
    print (llist.isEmpty())
    a = llist.valueAt(3)
    print ("Value at index 3 : ", end='')
    print (a)
    print ("Pop Front gives : ", end='')
    print (llist.popFront())
    print ("Pop Back gives : ", end='')
    print (llist.popBack())
    print ("Linked list thus far is...  ", end='')
    llist.printList()
    print ("Front : ", end='')
    print (llist.front())
    print ("Back : ", end='')
    print (llist.back())