def element():
    n=int(input())
    return n
def elemat(l):
    M=[]
    print("element for i =",end=" ")
    for j in range(l):
        M.append(element())
    return M        
  #variables:
n= int(input("no of elements "))
m=[]
for i in range(n):
    k=elemat(n)
    m.append(k)


print(m)    
            
