"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        temp = self.head
        while temp != None and position > 1:
            temp = temp.next
            position -= 1
        return temp if temp != None else None


    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        temp = self.head
        while temp != None and position > 2:
            temp = temp.next
            position -= 1
        next = temp.next
        temp.next = new_element
        new_element.next = next    
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        temp = self.head
        prev = None
        if temp.value == value:
            self.head = temp.next
        else:
            while temp:
                if temp.value == value:
                    prev.next = temp.next
                    break
                prev = temp
                temp = temp.next
