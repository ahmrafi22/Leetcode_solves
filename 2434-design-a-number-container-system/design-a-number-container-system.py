from collections import defaultdict
from sortedcontainers import SortedSet

class NumberContainers:
    def __init__(self):
        self.index_to_number = {}
        # Maps number to set of indices containing that number
        self.number_to_indices = defaultdict(SortedSet)
        
    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            self.number_to_indices[old_number].remove(index)
            
        # Update mappings
        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)
        
    def find(self, number: int) -> int:
        # Return smallest index containing the number, or -1 if none exists
        indices = self.number_to_indices[number]
        return indices[0] if indices else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)