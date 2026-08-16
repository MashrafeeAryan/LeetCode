class Allocator:
    """
    Instead of looping everytime, we can probably set up a pointer and kjust keep tract if we have enough space left
    """
    def __init__(self, n: int):
        self.memory = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        
        count = 0
        for i in range(len(self.memory)):
            if self.memory[i] == 0:
                count+=1
            else:
                count = 0
        
            if count == size:
                start_index = i - size + 1
                for j in range(start_index, start_index + size):
                    self.memory[j] = mID
                
                return start_index
        return -1

    def freeMemory(self, mID: int) -> int:
        count = 0
        for i in range(len(self.memory)):
            if self.memory[i] == mID:
                self.memory[i] = 0
                count+=1
        
        return count
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)