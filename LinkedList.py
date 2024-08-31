
class node:
     def __init__(self, data= None) :
          self.data =data
          self.next =None

class linked_list:
     def __init__(self):
          self.head = node()

     def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
          cur = cur.next
          cur.next = new_node

     def length(self):
        cur = self.head
        total = 0
        while cur.next!= None:
          total +=1 
          cur = cur.next
        return total

     def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next!= None:
          cur_node = cur_node.next 
          elements.append(cur_node.data)
        print elements

ll = linked_list()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

ll.display()

max_num = ll[0]

for i in range(1, len(ll)):
    if ll[i] > max_num:
        max_num = ll[i]

print(max_num)
















    


