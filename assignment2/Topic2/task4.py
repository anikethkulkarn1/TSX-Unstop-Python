#Task 4: to experiment with different arithmetic and logical operators

def arithmetic_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    modulus = a % b
    exponent = a ** b
    floor_division = a // b

    return addition, subtraction, multiplication, division, modulus, exponent, floor_division
def logical_operations(a, b):
    and_operation = a and b
    or_operation = a or b
    not_operation = not a

    return and_operation, or_operation, not_operation

arithmetic_operations_result = arithmetic_operations(10, 5)
logical_operations_result = logical_operations(True, False)
print("Arithmetic Operations Result:")
print("Addition:", arithmetic_operations_result[0])
print("Subtraction:", arithmetic_operations_result[1])
print("Multiplication:", arithmetic_operations_result[2])
print("Division:", arithmetic_operations_result[3])
print("Modulus:", arithmetic_operations_result[4])
print("Exponent:", arithmetic_operations_result[5])
print("Floor Division:", arithmetic_operations_result[6])
print("------------------------")
print("Logical Operations Result:")
print("AND:", logical_operations_result[0])
print("OR:", logical_operations_result[1])
print("NOT:", logical_operations_result[2])