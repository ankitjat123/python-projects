m=[]
k=[]
j=0

n=int(input("how many contact u want to save"))
for i in range (0,n):
    name =[input("enter the name ")]
    m=m+name
    number =[input("enter the number ")]
    k=k+number
y= str(input("enter the name which no u want search"))
while j <=n:
    if m[j]==y:
        print(k[j])
    j+=1    

    
a=input()
