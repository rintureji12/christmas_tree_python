import random
li=['*','~','+','0','^','.']
def base():
    for i in range(1,10):
        for j in range(1,12):
            print(" ",end="")
        for j in range(1,8):
            print("*",end="")
        print()    
def pyramid(start,end,flag):
    for i in range(start,end+1):
        for k in range(end-i):
            print(" ",end="")
        for j in range(1,2*i):
            if i==1:
                print("*",end="")
            else:
                print(random.choice(li),end="")
        if i==((start+end)//2) and flag==1:
            print("\tMerry christmas and happy new year",end="")    
        print()    
        
pyramid(1,15,1)  
pyramid(8,15,0)   
pyramid(6,15,0)       
base()            
