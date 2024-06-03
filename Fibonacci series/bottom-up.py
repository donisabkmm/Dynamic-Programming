"""
Fibonacci Series Bottom Up Approach

1 2 3 4 5 6 7  8  9
1 1 2 3 5 8 13 21 34

Find value of nth position
"""

def fibonacci(n):
    if n<=2:
        return 1
    fib_list = [0]*(n)
    fib_list[0] = 1
    fib_list[1] = 1
    for i in range(2, n):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    return fib_list[-1]

"""
Test cases
"""

test_cases = [
    {"test":[2,1]},
    {"test":[3,2]},
    {"test":[9,34]}
]

for test_case in test_cases:
    data = fibonacci(test_case["test"][0])
    if data == test_case["test"][1]:
        print(f"Passed {data}")
    else:
        print(f"Failed {data}")