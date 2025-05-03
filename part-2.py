# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    
    '''
    I: array - usorted array of strings; query - string value to find
    O: True - if query in array, False otherwise
    '''
    if not array:
        return False
        
    if array[0] == query:
        return True
    
    return search(array[1:], query)

# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    
    if text[0] != text[-1]:
        return False
    
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(apples, oranges):
    if apples == 0 and oranges == 0:
        return 1
    # If one or both are 1-digit numbers
    elif apples < 10 or oranges < 10:
        if apples % 10 == oranges % 10:
            return 1
        
        return 0
        
    last_digit_apples = apples % 10
    last_digit_oranges = oranges % 10

    match = 0
    if last_digit_apples == last_digit_oranges:
        match = 1
    
    return match + digit_match(apples // 10, oranges // 10)