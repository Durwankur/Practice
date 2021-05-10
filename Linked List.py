class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        
class Linked:
    def __init__(self):
        self.head = None
        
    def show(self):
        node = self.head
        while node is not None:
            print (node.data)
            node = node.next
link = Linked()

e1 = Node("dur")
link.head = e1
link.show()
link.head = Node('wan')
link.show()
