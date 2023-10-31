import math
def find_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
def find_gcd(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = math.gcd(result, num)
    return result
n = int(input("Enter the number of values: "))
values = []
for i in range(n):
    value = int(input(f"Enter value {i + 1}: "))
    values.append(value)
lcm = values[0]
gcd = values[0]
for value in values[1:]:
    lcm = find_lcm(lcm, value)
    gcd = math.gcd(gcd, value)
print(f"Largest Common Multiple (LCM) of the values: {lcm}")
print(f"Greatest Common Divisor (GCD) of the values: {gcd}")
