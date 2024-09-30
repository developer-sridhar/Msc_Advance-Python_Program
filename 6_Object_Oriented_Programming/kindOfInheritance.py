class Calculation1:
    def summation(self, a, b):
        return a + b  # Corrected the return statement

class Calculation2:
    def multiplication(self, a, b):
        return a * b  # Corrected the multiplication method

class Derived(Calculation1, Calculation2):
    def divide(self, a, b):
        return a / b  # Removed unnecessary semicolon

# Create an instance of the Derived class
d = Derived()

# Print results of the calculations
print("Summation:", d.summation(10, 20))        
print("Multiplication:", d.multiplication(10, 20))  
print("Division:", d.divide(10, 20))              

# OUTPUT
# Summation: 30
# Multiplication: 200
# Division: 0.5