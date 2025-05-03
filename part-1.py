# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("Input must be >= 0.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# reverse
def reverse(text):
    # return text[::-1]
    
    if text == "":
        return ""  # base case
        
    return reverse(text[1:]) + text[0] 

# bunny
def bunny(count):
    if count == 0:
        return 0
    
    return bunny(count - 1) + 2

# is_nested_parens
def is_nested_parens(parens):
    
    
    if parens == "":
        return True  # base case
        
    if parens[0] == '(' and parens[-1] == ')':
        return is_nested_parens(parens[1:-1])

    return False