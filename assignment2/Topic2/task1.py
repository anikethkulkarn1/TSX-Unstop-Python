#Task 1: Area and perimeter of a rectangle

def area(length, width):                    #defining a function
    length=float(length)                    
    width=float(width)
    area=length * width
    print("Area of rectangle is", area)
    return area

def perimeter(length, width):
    length=float(length)
    width=float(width)
    area=length * width
    print("Area of rectangle is", area)
    return area

def perimeter(length, width):
    length=float(length)
    width=float(width)      
    peri=2 * (length + width)
    print("Perimeter of rectangle is", peri)
    return peri

area(5, 10)                             #calling the function
perimeter(5, 10)



