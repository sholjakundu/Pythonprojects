"""
WAP to find the smallest, largest number from the list of entered numbers.
"""
n=[]
number=int(input("How many numbers are there:"))
for i in range(1,number+1):
    value=int(input("Enter number:"))
    n.append(value)
print("Largest element of the list is :", max(n))
print("Smallest element of the list is: ", min(n))
