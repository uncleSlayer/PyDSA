class Node():

    def __init__(self, value):

        self.value = value
        self.next = None
    

node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')

node_a.next = node_b
node_b.next = node_c
node_c.next = node_d

def find_target(head, target):

    current = head

    while current != None:

        if current.value == target:
            return True
        
        current = current.next
    
    return False

print(find_target(node_a, 'a'))
