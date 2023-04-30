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

def reverse_linked_list():

    prev = None
    current = node_one

    while current != None:

        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    print(node_one.next, node_two.next.value, node_three.next.value, node_four.next.value)


reverse_linked_list()