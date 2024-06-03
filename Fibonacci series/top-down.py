"""
Fibonacci Series Top Down Approach

1 2 3 4 5 6 7  8  9
1 1 2 3 5 8 13 21 34

Find value of nth position

Here the programming Algorithm we used is DFS Depth First Search
"""

def fibonacci(n,memory):
    if n in memory:
        return memory[n]
    if n <= 2:
        return 1
    memory[n] = fibonacci(n-1,memory)+fibonacci(n-2,memory)
    return memory[n]

"""
Test cases
"""

test_cases = [
    {"test":[2,1]},
    {"test":[3,2]},
    {"test":[9,34]}
]

for test_case in test_cases:
    data = fibonacci(test_case["test"][0],{})
    if data == test_case["test"][1]:
        print(f"Passed {data}")
    else:
        print(f"Failed {data}")