#!/usr/bin/python


class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        try:
            return self.stack.pop()
        except:
            return None

    def empty(self):
        if len(self.stack)==0: 
            return 1
        else:
            return 0

    def dump(self):
        print "STACK:", self.stack

class Queue:
    def __init__(self):
        self.queue=[]
    
    def push(self,x):
        self.queue.append(x)

    def dump(self):
        return ''.join(self.queue)

opp={ '^':(80,'r') , '*':(50,'l') , '/':(50,'l') , '+':(20,'l') , '-':(20,'l') , '(':(1,'d') }

def to_postfix(expr):
    rpn=''
    s=Stack()
    q=Queue()

    for i in expr:
        #s.dump()
        #print "QUEUE:",q.dump()
        #print "CURRENT:",i
        if i in '0123456789':
            q.push(i)
        elif i in '+-*/^':
            sop=s.pop()
            while sop and (( opp[i][0]<=opp[sop][0] and opp[i][1]=='l' ) or ( opp[i][0]<opp[sop][0] )):
                q.push(sop)
                sop=s.pop()
            if sop: s.push(sop)
            s.push(i)
            #s.dump()

        elif i in '()':
            if i=='(':
                s.push(i)
            else:
                sop=s.pop()
                while sop and sop!='(':
                    q.push(sop)
                    sop=s.pop()
                #if sop: s.push(sop)

    while not s.empty():
        q.push(s.pop())

    rpn=q.dump()

    return rpn



print to_postfix("2+7*5") ,' Should return "275*+"'
print to_postfix("3*3/(7+1)") ,' Should return "33*71+/"'
print to_postfix("5+(6-2)*9+3^(7-1)") ,' Should return "562-9*+371-^+"'
