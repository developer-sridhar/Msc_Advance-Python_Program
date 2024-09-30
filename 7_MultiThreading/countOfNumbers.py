from time import sleep, perf_counter
from threading import Thread

# Tuple of numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Counters for odd and even numbers
count_odd = 0
count_even = 0

# Counting odd and even numbers
for x in numbers:
    if not x % 2:
        count_even += 1
    else:
        count_odd += 1

def task():
    print('Starting a task...')
    print("Number of even numbers:", count_even)
    sleep(1.9)  # Sleep for 1.9 seconds
    print("Number of odd numbers:", count_odd)

# Measure time taken for task execution
start_time = perf_counter()
t1 = Thread(target=task)  # Create a thread for the task
t1.start()  # Start the thread
t1.join()  # Wait for the thread to finish
end_time = perf_counter()

# Print the time taken to complete the task
print(f'It took {end_time - start_time:0.2f} second(s) to complete.')


# OUTPUT:
# Starting a task...
# Number of even numbers: 4
# Number of odd numbers: 5
# It took 1.90 second(s) to complete.