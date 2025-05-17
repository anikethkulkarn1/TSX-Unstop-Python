#Task 2: comparision of two numbers

def compare(a, b):                     #defining a function
    a=float(a)
    b=float(b)
    if a > b:
        print(a, "is greater than", b)
    elif a < b:
        print(a, "is less than", b)
    else:
        print(a, "is equal to", b)
        return a,b
     
compare(5, 10)                       #calling the function