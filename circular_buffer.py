class order:
    def __init__(self, N):
        self.buffer=[None] * N
        self.cursor=0
        self.N=N
        
    def record(self,id):
        self.buffer[self.cursor]=id
        self.cursor+=1
        if self.cursor==self.N:
            self.cursor=0
            
    def get_last(self,i):
        location=self.cursor - i
        if location <0:
            location +=self.N
        return self.buffer[location]

x=order(3)
x.record("I")
x.record("like")
x.record("bananas")
print(x.get_last(0))
print(x.get_last(2))
print(x.get_last(1))
