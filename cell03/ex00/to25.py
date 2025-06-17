print("Enter a number less than 25")
num = int(input())

if num > 25:
    print("Error")
else:
    for x in range(num,26):
        print(f"Inside the loop, my variable is {x}")
    