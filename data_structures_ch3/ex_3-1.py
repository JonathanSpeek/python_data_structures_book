# Exercises 3.1
import time

problem_size = 100000
count = 1
start = time.time()

while problem_size > 0:
    print(count)
    count += 1
    problem_size = problem_size // 2
elapsed = time.time() - start

print(elapsed)
