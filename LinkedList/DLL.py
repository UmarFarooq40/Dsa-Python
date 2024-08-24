class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        tempnode = self.head
        result = ""
        while tempnode is not None:
            result += str(tempnode.value)
            if tempnode.next:
                result += " < ==== > "
            tempnode = tempnode.next
        return result

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        print(f"Appended {value}. New length: {self.length}")

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        print(f"Prepended {value}. New length: {self.length}")

    def Traversal(self):
        print("Forward Traversal:")
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def reverse_traversal(self):
        print("Reverse Traversal:")
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev

    def search(self, target):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                print(f"Found {target} at index {index}")
                return index
            current_node = current_node.next
            index += 1
        print(f"{target} not found in the list")
        return -1

    def get(self, index):
        print(f"Getting node at index {index}")
        if index < 0 or index >= self.length:
            print("Index out of bounds")
            return None

        if index < self.length // 2:
            print("Traversing from head")
            current_node = self.head
            for i in range(index):
                print(f"Moving to node {i+1}")
                current_node = current_node.next
        else:
            print("Traversing from tail")
            current_node = self.tail
            for i in range(self.length - 1, index, -1):
                print(f"Moving to node {i}")
                current_node = current_node.prev

        print(f"Returning node with value: {current_node.value}")
        return current_node

    def set_method(self, index, value):
        node = self.get(index)
        if node:
            old_value = node.value
            node.value = value
            print(f"Updated value at index {index} from {old_value} to {value}")
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Index out of bounds")
            return False

        new_node = Node(value)
        
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)

        temp_node = self.get(index - 1)
        if not temp_node:
            return False

        new_node.next = temp_node.next
        new_node.prev = temp_node
        if temp_node.next:
            temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1
        print(f"Inserted {value} at index {index}. New length: {self.length}")
        return True

    def pop_first(self):
        if self.length == 0:
            print("List is empty, cannot pop first element")
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        print(f"Popped first node with value: {popped_node.value}. New length: {self.length}")
        return popped_node

    def pop_last(self):
        if self.length == 0:
            print("List is empty, cannot pop last element")
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        print(f"Popped last node with value: {popped_node.value}. New length: {self.length}")
        return popped_node

    def remove(self, index):
        print(f"Attempting to remove node at index {index}")
        print(f"Current list length: {self.length}")

        if index < 0 or index >= self.length:
            print("Invalid index")
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop_last()
        
        popped_node = self.get(index)
        
        if popped_node is None:
            print("Node not found")
            return None
        
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        
        popped_node.next = None
        popped_node.prev = None
        
        self.length -= 1
        print(f"Removed node with value: {popped_node.value}. New length: {self.length}")
        return popped_node

# Test the LinkedList
dll = LinkedList()
dll.append(10)
dll.append(100)
dll.prepend(500)
dll.append(100)
dll.append(1000)

print("\nForward Traversal:")
dll.Traversal()

print("\nReverse Traversal:")
dll.reverse_traversal()

print("\nSearching for 1000:")
dll.search(1000)

print("\nUpdating value at index 4:")
dll.set_method(4, 999)

print("\nTrying to insert at invalid index:")
dll.insert(52, 888)

print("\nRemoving node at index 1:")
dll.remove(1)

print("\nFinal list:")
print(dll)