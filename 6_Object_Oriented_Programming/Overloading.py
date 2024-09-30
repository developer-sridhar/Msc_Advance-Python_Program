class Bubble:
    def __init__(self, volume):
        self.volume = volume

    def __add__(self, other):
        if isinstance(self.volume, (int, float)) and isinstance(other.volume, (int, float)):
            # Only add if both volumes are numeric
            new_volume = self.volume + other.volume
            return Bubble(new_volume)  # Return a new instance of Bubble with the combined volume
        else:
            # Handle non-numeric volumes
            return Bubble(str(self.volume) + str(other.volume))  # Concatenate strings

# Create instances of Bubble
b1 = Bubble(20)
b2 = Bubble(30)
b3 = Bubble("Hello")
b4 = Bubble("World")

# Print the results of the additions
print((b1 + b2).volume)  
print((b3 + b4).volume) 


#OUTPUT
# 50
# HelloWorld