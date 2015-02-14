#!/usr/bin/python


def calc(expr):
    #print expr
    stack=[]
    if not expr: return 0 
    for i in expr.split():
        #print i,stack
        if i in '+-*/':
            o2=str(stack.pop())
            o1=str(stack.pop())
            e=o1+str(i)+o2
            stack.append(eval(e))
        else:
            try:
                o=int(i)
            except ValueError:
                print i,"Not an int"
                try:
                    o=float(i)
                except ValueError:
                    print i,"Not a float"
            print o,' == ',type(o)
            stack.append(o)
    return stack[-1]


print calc('5 1 2 + 4 * + 3 -')
print "5 + ((1 + 2) * 4) - 3 == 14"

print calc("") ," 0, Should work with empty string"
print calc("1 2 3") ," 3, Should parse numbers"
print calc("1 2 3.5") ," 3.5, Should parse float numbers"
print calc("1 3 +") ," 4, Should support addition"
print calc("1 3 *") ," 3, Should support multiplication"
print calc("1 3 -") ," -2, Should support subtraction"
print calc("4 2 /") ," 2, Should support division"
