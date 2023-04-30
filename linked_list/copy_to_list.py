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

transfer_data = []


def copy_data(head):
    
    current = head

    while current != None:

        transfer_data.append(current.value)

        current = current.next

    print(transfer_data)


copy_data(a)