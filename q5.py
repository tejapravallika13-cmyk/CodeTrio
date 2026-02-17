def calculate(expression: str) -> float: 
    s = expression.replace(" ", "") + "+" 
    stack, num, op = [], 0, "+" 
    for i, c in enumerate(s): 

        if c.isdigit(): 
            num = num*10 + int(c) 

        elif c in "+-*/": 
            if op == "+": stack.append(num) 
            elif op == "-": stack.append(-num) 
            elif op == "*": stack[-1] *= num 
            elif op == "/": stack[-1] /= num
            op, num = c, 0 
    return round(sum(stack), 2) 

Teamname-{CodeTrio}
