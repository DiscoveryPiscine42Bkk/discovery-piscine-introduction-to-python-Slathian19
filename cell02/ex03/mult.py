num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print(f"{num1} x {num2} = {num1 * num2}")
if num1 * num2 > 0 :
    print("the result is positive.")
elif num1 * num2 < 0:
    print("the result is negative.")
else :
    print("the result is positive and negative.")