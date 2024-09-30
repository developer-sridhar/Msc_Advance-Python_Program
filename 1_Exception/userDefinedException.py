class PercentageError(Exception):
    pass

class InvalidPercentageError(PercentageError):
    def __init__(self):
        super().__init__("Percentage is invalid")

class LessPercentageError(PercentageError):
    def __init__(self):
        super().__init__("The percentage is lesser than the cut-off. Please try again.")

class checkPercentage:
    def __init__(self, per):
        if per < 80:
            raise LessPercentageError
        elif per > 100:
            raise InvalidPercentageError
        else:
            print("Congrats, you're Enrolled")

try:
    print("For percentage: 93")
    checkPercentage(93)
except Exception as e:
    print(e)

try:
    print("\nFor percentage: 102")
    checkPercentage(102)
except Exception as e:
    print(e)

try:
    print("\nFor percentage: 58")
    checkPercentage(58)
except Exception as e:
    print(e)


#OUTPUT
# For percentage: 93
# Congrats, you're Enrolled

# For percentage: 102
# Percentage is invalid

# For percentage: 58
# The percentage is lesser than the cut-off. Please try again.