class Node:

    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head_val = None

    def create_node(self, data):
        node_obj = Node(data)
        return node_obj

    def traverse_dll(self):
        if self.head_val is None:
            print("Doubly Linkedlist is not defined.")

        head = self.head_val
        while head is not None:
            print(head.data)
            head = head.next

    def insert_node_at_beginning(self, data):
        node_obj = self.create_node(data)
        node_obj.next = self.head_val
        self.head_val = node_obj

    def insert_node_in_between(self, insert_after_elem, data):
        node_obj = self.create_node(data)
        node_obj.next = insert_after_elem.next
        node_obj.prev = insert_after_elem
        insert_after_elem.next = node_obj

    def insert_at_end(self, data):
        head = self.head_val
        while head is not None:
            last_element = head
            head = head.next
        node_obj = self.create_node(data)
        node_obj.prev = last_element
        last_element.next = node_obj


linkedlist = DoublyLinkedList()
node_a = Node("A")
node_c = Node("C")

node_a.next = node_c
node_c.prev = node_a

linkedlist.head_val = node_a
linkedlist.insert_node_in_between(node_a, "B")
linkedlist.insert_at_end("D")
linkedlist.traverse_dll()
