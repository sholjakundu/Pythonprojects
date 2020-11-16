"""
WAP to find the even, odd no. from the list of entered values
"""
n=[]
num=int(input("Enter the total number of list elements: "))
for i in range(1,n+1):
    value=int(input("please enter the element:"))
    n.append(value)
even=[]
odd=[]
for j in n:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list ",even)
print("The odd list ",odd)