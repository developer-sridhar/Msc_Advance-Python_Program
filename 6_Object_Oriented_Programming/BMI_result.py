class Person:
    def __init__(self, name='', age=0, height=0, weight=0):
        self.name = name 
        self.age = age
        self.height = height
        self.weight = weight

    def BMI_result(self):
        self.BMI = self.weight / (self.height / 100) ** 2  # BMI calculation
        print("Your body mass index is", self.BMI)
        
        # BMI classifications
        if self.BMI <= 18.5:
            print("Oops! You are underweight")
        elif self.BMI <= 24.9:
            print("Awesome! You are healthy")
        elif self.BMI <= 29.9:
            print("Eee! You are overweight")
        else:
            print("Seesh! You are obese")

# Create an instance of the Person class
p1 = Person('Sridhar', 20, 159, 48)  # Pass parameters directly to the constructor
p1.BMI_result()  # Call the method to display BMI and classification


# OUTPUT
# Your body mass index is 18.986590720303784
# Awesome! You are healthy