#This program is for implementing queue.
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



#  Changed by vivek 
class queue_himanshu:
    def __init__(self):
        self.value=[]
    
    def enqueue(self,value):
        print("you push :",value)
        self.value.append(value)
        
    


 # type: ignore

 class equeue_himanshu:
    def __init__(self):
        self.value=[]
    
    def enqueue(self,value):
        print("you push :",value)
        self.value.append(value)
        
    