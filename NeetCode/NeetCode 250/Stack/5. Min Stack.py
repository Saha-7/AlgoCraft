class MinStack:

    def __init__(self):
        self.stak = []
        self.minStak = []

    def push(self, val: int) -> None:
        self.stak.append(val)

        if self.minStak==[]:
            self.minStak.append(val)
        elif self.minStak[-1] < val:
            self.minStak.append(self.minStak[-1])
        else:
            self.minStak.append(val)

    def pop(self) -> None:
        self.stak.pop()
        self.minStak.pop()

    def top(self) -> int:
        return self.stak[-1]

    def getMin(self) -> int:
        return self.minStak[-1]
        


sol = MinStack()