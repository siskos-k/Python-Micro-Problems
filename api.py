
def check_divisible(num):
    if num % 3 == 0 and num % 4 == 0:
        print("True")
    else:
        print("False")

try:
    user_input = int(input("Enter a number: "))
    check_divisible(user_input)
except ValueError:
    print("Invalid input. Please enter an integer.")
# check_divisible(user_input)
