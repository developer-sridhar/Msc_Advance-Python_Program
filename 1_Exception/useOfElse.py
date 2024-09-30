try:
    X = int(input("Enter a number: "))
except:
    print("An error occurred!")
else:
    print("The number entered is", X)
finally:
    print("Program ended")
    
#OUTPUT
# Enter a number: a
# An error occurred!
# Program ended 

# # Enter a number: 20
# The number entered is 20
# Program ended
