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
            temp=temp.next
    def append(self,value):
        new_node=node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    
        self.length+=1

my_linked_list=linked_list(2)
my_linked_list.append(5)
my_linked_list.append(7)
my_linked_list.append(9)
my_linked_list.print_list()