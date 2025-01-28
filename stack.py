class stack:
    def __init__(self):
        self.value=[]
    
    def push(self,value):
        print("push",value)
        self.value=[value]+self.value
        
    def pop(self):
        if len(self.value)==0:
            print("stack is empty")
        else:
            n=len(self.value)
            first=self.value[n-1]
            print("pop",first)
            self.value=self.value[:-1]
            
        
    def printvalue(self):
        print("stack is : ")
        for i in self.value:
            print(i,end=" ")

    def top(self):
        first=self.value[0] 
        print("top is ",first)
            
q=stack()
q.pop()
q.push(5)
q.push(6)
q.pop()
q.push(7)
q.push(8)
q.pop()
q.top()
q.printvalue()


class himu:
    def __init__(self):
        self.value=[]
    
    def push(self,value):
        print("push",value)
        self.value=[value]+self.value
        
    def pop(self):
        if len(self.value)==0:
            print("stack is empty")
        else:
            n=len(self.value)
            first=self.value[n-1]
            print("pop",first)
            self.value=self.value[:-1]
            
        
    def printvalue(self):
        print("stack is : ")
        for i in self.value:
            print(i,end=" ")

    def top(self):
        first=self.value[0] 
        print("top is ",first)