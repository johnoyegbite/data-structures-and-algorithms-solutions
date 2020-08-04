# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 06:39:14 2019

@author: John Oyegbite
"""
# SOLVED!


def has_higher_precedence(operator_1:str, operator_2:str)->bool:
    operator_value = {"^": 5, "/": 4, "*": 4, "-": 2, "+": 2}
    return operator_value[operator_1] == operator_value[operator_2] or \
                operator_value[operator_1] > operator_value[operator_2]


def is_opening_parentheses(operator):
    return operator == "("


def is_closing_parentheses(operator):
    return operator == ")"


def stack_not_empty(stack):
    return len(stack) > 0


def infix_to_postfix(infix: str) -> str:
    """
    Note:
    -> 4+*6 would give syntax error
    -> 4*+6 would give 24 => 4 * (+9)
    
    Write a function to replace all multiple in infix of the from
       1. replace *+ with *
       
    """
    # infix = replace_multiples(infix)
    postfix_str = ""
    operator_stack = []
    operators = ["+", "-", "*", "/", "^"]
    # Traverse through the string.
    for char in infix:
        if char in operators:
            if stack_not_empty(operator_stack):
                top_operator = operator_stack[-1]
                new_operator = char
                while stack_not_empty(operator_stack) and \
                    (not is_opening_parentheses(top_operator))\
                    and has_higher_precedence(top_operator, new_operator):
                    operator_removed = operator_stack.pop()
                    postfix_str += operator_removed
                    if stack_not_empty(operator_stack):
                        top_operator = operator_stack[-1]
                operator_stack.append(new_operator)
            else:
                operator_stack.append(char)
        elif is_opening_parentheses(char):
            operator_stack.append(char)
        elif is_closing_parentheses(char):
            if stack_not_empty(operator_stack):
                top_operator = operator_stack[-1]
                while stack_not_empty(operator_stack) and \
                    (not is_opening_parentheses(top_operator)):
                    operator_removed = operator_stack.pop()
                    postfix_str += operator_removed
                    if stack_not_empty(operator_stack):
                        top_operator = operator_stack[-1]
                 # You have to remove the corresponding open parentheses
                 # from the stack.
                if stack_not_empty(operator_stack):
                    operator_stack.pop()
        else:
            postfix_str += char
    # Put any remaining operator in the string
    while stack_not_empty(operator_stack):
        operator_removed = operator_stack.pop()
        postfix_str += operator_removed
    return postfix_str


if __name__ == "__main__":
    infix = "(1+2)*(3-4)*(5+9)"
    infix = "6*3/2*5"
    infix = "6*3/2*5*1+(2*3+4)^5+9"
    infix = "2*4+5*(6^3+1)"
    print(infix_to_postfix(infix))