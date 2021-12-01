# Exercício Programa I – MAC 122 – PDA
# Heloisa Tambara 
import re
from pile import pile
from fractions import fraction

def pri(x): # priorities of operators
    if x == '+': return 1
    elif x == '-': return 1
    elif x == '*': return 2
    elif x == '/': return 2
    elif x == '**': return 3
    elif x == '(': return 4 
    elif x == ')': return 5 
    else: return 0 # it's not an operator

def op(num1, operator, num2): # operations with strings
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '**':
        return num1 ** num2


# starters
def postfixTranslator(expr): # creating the expression
    exprli = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", expr) # gives a list with the strings in the expression
    oppile = pile() # operator pile
    pexpr = [] # postfix expression list

    
    for k in range(len(exprli)-1): # transforms the power simbols in one simbol
        if exprli[k] == '*' and exprli[k+1] == '*':
            exprli[k] = '**'
            del exprli[k+1]

    for k in range(len(exprli)): # transforms number strings in int
        if '0' < exprli[k][0] < '9':
            exprli[k] = int(exprli[k])


    for k in range(len(exprli)):
        p = exprli[k]
        if type(p) == int: # if it's a number
            pexpr.append(exprli[k])
        elif  0 < pri(p) < 4 : # if it's an operator
            while len(oppile) > 0:
                if 4 > pri(oppile.top()) >= pri(p): 
                    pexpr.append(oppile.pop()) # put on the postfix all operators with greater or equal priority and pop them out of the pile
                else:
                    break
            
            oppile.stack(p) # stack the new operator

        if pri(p) == 4: # if it's an open parenthesis
            oppile.stack(p)
        if pri(p) == 5: # if it's a close parenthesis
            while len(oppile) > 0:
                pexpr.append(oppile.pop()) # put on the postfix all operators inside the parenthesis and pop them out of the pile
                if pri(oppile.top()) == 4:
                    oppile.pop() # pop the open parenthesis
                    break


    while len(oppile) > 0:
        pexpr.append(oppile.pop()) # put on the postfix all the operators left
    
    return pexpr


def postfixCalculator(listexp): # calculating after reading
    pexpr = postfixTranslator(listexp)
    for k in range(len(pexpr)):
        if type(pexpr[k]) == int:
            pexpr[k] = fraction(pexpr[k])

     
    # read the expression
    while len(pexpr) > 1:
        for k in range(len(pexpr)):
            if pri(pexpr[k]) > 0:
                aux = op(pexpr[k-2], pexpr[k], pexpr[k-1])
                pexpr[k-2] = aux
                del pexpr[k-1]
                del pexpr[k-1]
                break
    return pexpr[0]

def main():
    while True:
        t = input()
        print(TraduzPosFixa(t))
        print(CalculaPosFixa(t))

main()
