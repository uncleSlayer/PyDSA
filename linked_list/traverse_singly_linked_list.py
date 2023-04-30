class Node():

    def __init__(self, value):

        self.value = value
        self.next = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d


def print_linked_list(head):
    
    current = head

    while current != None:

        print(current.value)

        current = current.next

print_linked_list(a)

