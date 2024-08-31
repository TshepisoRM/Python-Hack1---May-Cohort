class QueueWithStack:

    def __init__(self):
            self.firstData = []
            self.secondData = []

    def push(self, x: int) -> None:
          self.firstData.append(x)

    def pop(self) -> int:
          if not self.secondData:
                while self.firstData:
                      self.secondData(self.firstData.pop())
                return self.secondData.pop()
          
    def peek(self) -> int:
           if not self.secondData:
                while self.firstData:
                      self.secondData(self.firstData.pop())
                return self.secondData[-1]
           
    def empty(self) -> bool:
          return max(len(self.firstData),  len(self.secondData))
          

