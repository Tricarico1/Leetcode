class MinStack:

    def __init__(self):
        self.stck = []
        self.minstck =[]


    def push(self, val: int) -> None:
        self.stck.append(val)
        val = min(val, self.minstck[-1] if self.minstck else val)
        self.minstck.append(val) 
        

    def pop(self) -> None:
        self.stck.pop()
        self.minstck.pop()
        

    def top(self) -> int:
        return self.stck[-1]

    def getMin(self) -> int:
        return self.minstck[-1]


        
