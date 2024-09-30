programming_Languages = ["Python", "JavaScript", "C++", "Java"]
indices = [0, 1, "2", 3]

for i in range(len(indices)):
    try:
        print(programming_Languages[indices[i]])
    except TypeError:
        print("TypeError: Check the list of indices")

#OUTPUT
# Python
# JavaScript
# TypeError: Check the list of indices
# Java