def valid_parentheses(string):
    # your code here
    checker = 0

    if string == "":
        return True
    
    for char in string:
        if char == "(":
            checker += 1
        if char == ")":
            checker -= 1
            if checker < 0:
                return False

    if checker == 0:
        return True
    else:
        return False

print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses(""))
print(valid_parentheses("hi())("))
print(valid_parentheses("hi(hi)()"))
        
