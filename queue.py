class queue:
    def __init__(self):
        self.value=[]
    
    def enqueue(self,value):
        print("you push :",value)
        self.value.append(value)
        
    def dequeue(self):
        if len(self.value)==0:
            print("queue is empty")
        else:
            front=self.value[0]
            print("remove",front)
            self.value=self.value[1:]
            
    def printvalue(self):
        print("queue is : ")
        for i in self.value:
            print(i,end=" ")
          
q=queue()
q.dequeue()  
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.dequeue()
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
q.enqueue(7)
q.dequeue()
q.printvalue()


<<<<<<< HEAD
 # type: ignore

#  Changed by vivek 
=======
class queue_himanshu:
    def __init__(self):
        self.value=[]
    
    def enqueue(self,value):
        print("you push :",value)
        self.value.append(value)
        
    def dequeue(self):
        if len(self.value)==0:
            print("queue is empty")
        else:
            front=self.value[0]
            print("remove",front)
            self.value=self.value[1:]
            
    def printvalue(self):
        print("queue is : ")
        for i in self.value:
            print(i,end=" ")


 # type: ignore
>>>>>>> 736c918dca1e832c23355c9dabe8024d020d7e5c
