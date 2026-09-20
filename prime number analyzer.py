# Function to check prime number
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


# Prime Checker
num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")


# Prime Number Range Generator
start = int(input("\nEnter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers are:")

for i in range(start, end + 1):
    if is_prime(i):
        print(i, end=" ")