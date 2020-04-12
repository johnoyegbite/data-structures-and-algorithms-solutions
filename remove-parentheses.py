# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:47:04 2019

@author: John Oyegbite
"""
# SOLVED!
"""
Problem:
    Given a string str consisting of parentheses (, ) 
    and alphanumeric characters. 
    Remove minimum number of paranthesis to make the string valid 
    and return any valid result. 
    In a valid string for every opening/closing parentheses there is a
    matching closing/opening one.

Example 1:
    Input: "ab(a(c)fg)9)"
    Output: "ab(a(c)fg)9" or "ab(a(c)fg9)" or "ab(a(cfg)9)"

Example 2:
    Input: ")a(b)c()("
    Output: "a(b)c()"

Example 3:
    Input: ")("
    Output: ""

Example 4:
    Input: "a(b))"
    Output: "a(b)"

Example 5:
    Input: "(a(c()b)"
    Output: "a(c()b)" or "(ac()b)" or "(a(c)b)"

Example 6:
    Input: "(a)b(c)d(e)f)(g)"
    Output: "(a)b(c)d(e)f(g)"
"""
# solution:
#          1. scan from left to right
#          2. if opening symbol push the position/character into the stack
#          3. if closing symbol is the same "character type" at end of stack, 
#             pop from stack (remove from the end).
#          4. if (3.) above is not valid, add the position to the invalid list 
#          5. at the end of the string, stack should be empty.
#          6. if not empty then the parentheses at those position in the stack
#             is invalid. Add to invalid list.
#          7. Remove invalid positional character from s.
def remove_parentheses(s):
    s = list(s)
    p_face_left = ")"
    p_face_right = "("
    stack = []
    invalid_paren = []
    for i in range(len(s)):
        if s[i] == p_face_right:
            # stack.append((p_face_right, i)) # store the type of parentheses
            stack.append(i) # just store the position since we don't have other types of parentheses
        elif s[i] == p_face_left:
            if len(stack) > 0:
                stack.pop()
            else:
                # invalid_paren.append((p_face_left, i)) # store parentheses that are not valid
                invalid_paren.append(i) # just store the position
    invalid_paren.extend(stack)
    valid_s = []
    for i in range(len(s)):
        if i not in invalid_paren:
            valid_s.append(s[i])
    return ''.join(valid_s)
    

if __name__ == "__main__":
    Input =  "ab(a(c)fg)9)"
    # Output = "ab(a(c)fg)9" or "ab(a(c)fg9)" or "ab(a(cfg)9)"
    
    Input = ")a(b)c()("
    # Output: "a(b)c()"
    
    Input = "a(b))"
    # Output: "a(b)"
    
    Input = "(a(c()b)"
    # Output: "a(c()b)" or "(ac()b)" or "(a(c)b)"
    
    Input = "(a)b(c)d(e)f)(g)"
    # Output: "(a)b(c)d(e)f(g)"
    print(remove_parentheses(Input))
    