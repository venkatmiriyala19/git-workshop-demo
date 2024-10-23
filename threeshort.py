OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2}

def infix_to_postfix(formula):
    stack, output = [], ""
    for char in formula:
        if char not in OPERATORS:
            output += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRECEDENCE[char] <= PRECEDENCE[stack[-1]]:
                output += stack.pop()
            stack.append(char)
    while stack:
        output += stack.pop()
    return output

def infix_to_prefix(formula):
    stack, output = [], []
    for char in formula:
        if char not in OPERATORS:
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack[-1] != '(':
                output.append(stack.pop() + output.pop() + output.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRECEDENCE[char] <= PRECEDENCE[stack[-1]]:
                output.append(stack.pop() + output.pop() + output.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop() + output.pop() + output.pop())
    return output[-1]

def generate_three_address_code(postfix):
    output, temp_var = [], 1
    for char in postfix:
        if char not in OPERATORS:
            output.append(char)
        else:
            print(f"t{temp_var} := {output[-2]} {char} {output[-1]}")
            output[-2:] = [f"t{temp_var}"]
            temp_var += 1

# Main program with dynamic input
expression = input("Enter the expression: ")
print("PREFIX:", infix_to_prefix(expression))
postfix = infix_to_postfix(expression)
print("POSTFIX:", postfix)
generate_three_address_code(postfix)
