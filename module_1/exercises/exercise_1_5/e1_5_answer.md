**Python Code**
```python
def count_paths(n, memo=None):
    # initialize cache once
    if memo is None:
        memo = {}

    # if we already solved this subproblem, reuse it
    if n in memo:
        return memo[n]

    # base cases (known answers)
    if n == 1:
        return 1
    if n == 2:
        return 2

    # recursive case:
    # number of ways to reach n is:
    # ways to reach n-1 plus ways to reach n-2
    memo[n] = count_paths(n-1, memo) + count_paths(n-2, memo)

    return memo[n]

print('count_paths(1) =', count_paths(1))
print('count_paths(2) =', count_paths(2))
print('count_paths(3) =', count_paths(3))
print('count_paths(4) =', count_paths(4))
print('count_paths(5) =', count_paths(5))
print('count_paths(6) =', count_paths(6))

# Example: using dictionary from former function call
print('count_paths(6) (test) =', count_paths(6, {6:13}))
```

**Console Output**
```
(.venv) C:\Projects\cs_foundations_for_agentic_multimodal_ai>python C:\Projects\cs_foundations_for_agentic_multimodal_ai\module_1\exercises\exercise_1_5\e1_5_answer.py
count_paths(1) = 1
count_paths(2) = 2
count_paths(3) = 3
count_paths(4) = 5
count_paths(5) = 8
count_paths(6) = 13
count_paths(6) (test) = 13
```