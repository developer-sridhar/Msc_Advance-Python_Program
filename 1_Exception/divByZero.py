def sample(num):
    try:
        div = 1 / num
    except ZeroDivisionError:
        print("We cannot divide by zero")
    else:
        print(div)

num = int(input("Enter the number: "))
sample(num)

#OUTPUT
# Enter the number: 0
# We cannot divide by zero