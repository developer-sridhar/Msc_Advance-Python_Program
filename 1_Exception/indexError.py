import sys
try:
    my_list = [3, 7, 9, 4, 6]
    print(my_list[6])
except IndexError as e:
    print("Index Error: ",e)

print(sys.executable)


#OUTPUT
# Index Error:  list index out of range