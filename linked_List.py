import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None                        
        
    def __repr__(self):
        return self.data

class Linkedlist:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data = elem)
                node = node.next
        
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next      
        
    # Method for traversing the linked list   
    
    def show_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end = " -> ")
            current_node = current_node.next
        print("None")

    # Method to add an item to the top of a linked list   
               
    def add_first(self, node):
        node.next = self.head
        self.head = node    

    # Method to add an item to the end of the linked list   
    
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node   

    # Method to add a node after a specific element in the linked list.
        
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    # Method to add a node before a specific element in the linked list.   
    
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    # Method to delete a node in the linked list

    def remove_node_data(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    # Method to return an element from a specific position in the linked list.
    
    def get_data(self, target_node_position):
        if self.head is None:
            raise Exception("List is empty")
           
        current_node = self.head
        num_element = 0
        
        for node in self:
            if num_element == target_node_position:
                return node.data
            
            current_node = current_node.next
            num_element += 1
            
        raise Exception("Node with position '%s' not found" % target_node_position)

    # Method to invert the linked list
    
    def reverse(self):
        if self.head is None:
            raise Exception("List is empty")
        
        current_node = self.head
        previous_node = None
        
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node              
            previous_node = current_node                   
            current_node = next_node
            
        self.head = previous_node

    # Method to remove the element from a specific position in the linked list
    
    def remove_node_position(self, target_node_position):
        if self.head is None:
            raise Exception("List is empty")
        
        if  target_node_position == 0:
            self.head = self.head.next
            return

        position = 0
        previous_node = self.head
        for node in self:
            if position == target_node_position:
                previous_node.next = node.next
                return
            position += 1
            previous_node = node
            
        raise Exception("Node with position '%s' not found" % target_node_position)
    
    
# Simulation queue cinema

age_people = random.randint(5, 60)
num_people = random.randint(0,50)

cinema_list = Linkedlist()
people_list = []
total = 0

for person in range(num_people):
    age_people = random.randint(5, 60)
    people_list.append(age_people)
    
for age in people_list:
    cinema_list.add_last(Node(age))
    
cinema_list.show_list()
    
for data in range(num_people):
    if (cinema_list.get_data(data) >= 5 and cinema_list.get_data(data) <= 10):
        total += 1
    elif (cinema_list.get_data(data) >= 11 and cinema_list.get_data(data) <= 17):
        total += 2.5
    else:
        total += 3.5
        
for remove in range(num_people):
    cinema_list.remove_node_position(0)
    cinema_list.show_list()

print("The total in the cinema is:",total)
