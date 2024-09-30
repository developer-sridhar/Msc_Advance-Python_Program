try:
    a = int(input("Enter a positive integer: ")) 
    if a <= 0:
        raise ValueError("This is not a positive integer!")
except ValueError as e:
    print(e)


# OUTPUT
# Enter a positive integer: -1
# This is not a positive integer!