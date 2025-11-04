class SinglyNodedLinkedList:

    def __init__(self, value, next=None ):
        
        self.value = value
        self.next = next 


    def __str__(self):
        return str(self.value)
    

head  = SinglyNodedLinkedList(1)
a = SinglyNodedLinkedList(10)
b = SinglyNodedLinkedList(77)
c = SinglyNodedLinkedList(7)

head.next = a 
a.next = b
b.next = c 

print(b.next)



# O(n)
def visualDisplayOfLinkedList(Head):
    firstElement = Head
    elements = []
    while firstElement:
        elements.append(str(firstElement.value))
        firstElement = firstElement.next 

    print('-->'.join(elements))

visualDisplayOfLinkedList(head)