class NumberContainers:

    def __init__(self):
        def heap_factory():
            return []
        self.index=dict()
        self.number=defaultdict(heap_factory)

    def change(self, index: int, number: int) -> None:
        self.index[index]=number
        heappush(self.number[number],index)
    def find(self, number: int) -> int:
        while self.number[number]:
            idx=heappop(self.number[number])
            if self.index[idx]==number:
                heappush(self.number[number],idx)
                return idx
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)