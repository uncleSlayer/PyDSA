class Node():

    def __init__(self, value):

        self.value = value
        self.next = None
        

node_one = Node('a')
node_two = Node('b')
node_three = Node('c')
node_four = Node('d')

node_one.next = node_two
node_two.next = node_three
node_three.next = node_four

def find_index(index):

    counter = 0

    current = node_one

    while current != None:

        if counter == index:
            return current.value
        
        counter += 1
        current = current.next
    
    return 'not found'


print(find_index(1))