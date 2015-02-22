#!/usr/bin/python

ct={ 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }


# dijkstras shunting-yard 
def solution(string):
    rom=string.upper()
    num=0
    buf=0
    for i in rom:
        if buf==0: 
            buf=i
        else:
            if ct[i]>ct[buf]: 
                num+=ct[i]-ct[buf]
                buf=0
            else:
                num+=ct[buf]
                buf=i
    if buf!=0: num+=ct[buf]
    return num


print solution('I'), '1'
print solution('IX'), '9'
print solution('VIII'), '8'
print solution('MCMLXXXIV'), '1984'
