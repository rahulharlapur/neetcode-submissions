class MinStack:

    def __init__(self):
        self.arr = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        

    def pop(self) -> None:
        self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        min_val = float('inf')
        for num in self.arr:
            min_val = min(min_val,num)
        return min_val
