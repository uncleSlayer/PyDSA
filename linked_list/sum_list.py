class Node():

    def __init__(self, value):

        self.value = value
        self.next = None


node_one = Node(1)
node_two = Node(2)
node_three = Node(3)
node_four = Node(4)

node_one.next = node_two
node_two.next = node_three
node_three.next = node_four

sum_list_value = 0

def sum_list(head, sum_list_value):

    current = head

    while current != None:

        sum_list_value += current.value

        current = current.next


    print(sum_list_value)


sum_list(node_one, sum_list_value)
