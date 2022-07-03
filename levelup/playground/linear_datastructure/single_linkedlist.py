class Node():
 def __init__(self, data):
  self.data = data
  self.next = None

class LinkedList():
 def __init__(self):
  self.headval = None

 def print_val(self):
  current_obj = self.headval
  while current_obj is not None:
   print(current_obj.data)
   current_obj = current_obj.next

 def insert_at_beginning(self, data):
  new_node = Node(data)
  if self.headval is not None:
   new_node.next = self.headval
   self.headval = new_node

 def insert_at_end(self, data):
  new_node = Node(data)
  if self.headval is not None:
   last_element = self.headval
   while last_element.next is not None:
    last_element = last_element.next
   last_element.next = new_node
  else:
   self.headval = new_node

 def insert_in_between(self, middle_elem, data):
  if middle_elem is None:
   return
  new_node = Node(data)
  new_node.next = middle_elem.next
  middle_elem.next = new_node

 def delete_element(self, data):
  head = self.headval
  if head is None:
   print("Empty linkedlist")
  else:
   if head.data == data:
    self.headval = self.headval.next
    head = None
    return
   else:
    while head.next is not None:
     if head.data == data:
      break
     prev = head
     head = head.next

  if head is None:
   print("No  such  data in a node")
   return
  prev.next = head.next
  head = None

slink_obj = LinkedList()
e1=Node("Mon")
e2=Node("Tues")
e3=Node("Wed")
slink_obj.headval = e1
e1.next=e2
e2.next=e3

slink_obj.insert_at_beginning("Sun")
slink_obj.insert_at_end("Fri")
slink_obj.insert_in_between(e3,"Thu")
# slink_obj.print_val()
slink_obj.delete_element("Mon")
slink_obj.print_val()