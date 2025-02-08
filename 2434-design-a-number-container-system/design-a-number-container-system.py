class NumberContainers:
    def __init__(self):
        self.idx_map = {}
        self.num_to_indices = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        # Store new mapping and add to heap
        self.idx_map[index] = number
        heappush(self.num_to_indices[number], index)

    def find(self, number: int) -> int:
        heap = self.num_to_indices[number]
        
        
        while heap:
            idx = heap[0]  # Peek at smallest index without popping
            if self.idx_map.get(idx, None) == number:
                return idx
            heappop(heap)  
            
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)