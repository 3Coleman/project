# A linked list is a collection of nodes where each node contains data and a reference (or link) to the next node. This structure allows for efficient insertions and deletions because you only need to adjust a few pointers.

# In contrast, a normal list in Python (an array) stores elements in contiguous memory, allowing for quick access by index but potentially costly insertions and deletions due to the need to shift elements around.

# Comparison:

# Storage:

# Linked List: Nodes are scattered in memory, with each node pointing to the next one.
# Python List: Elements are stored in a contiguous block of memory.
# Access Time:

# Linked List: Accessing an element requires traversing from the start, making it slower for random access.
# Python List: Provides direct access to elements via indices, which is faster.
# Insertion/Deletion:

# Linked List: Efficient as it only requires changing a few pointers.
# Python List: Less efficient because it often requires shifting elements to accommodate changes.
class node:
    def __init__(self,value):
        self.value=value
        self.next=None
class linked_list:
    def __init__(self,value):
        new_node=node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp.next
my_linked_list=linked_list(5)

print(my_linked_list.print_list())
