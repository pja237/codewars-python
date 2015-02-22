#!usr/bin/python

cte={ 1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M' }
cta=[1,10,100,1000]
ctax=[1000,500,100,50,10,5,1]

def solution(num):
    rom=''
    while num>0:
        #print num, cta[len(str(num))-1]
        tmp=(num/cta[len(str(num))-1])*cta[len(str(num))-1]
        if tmp in cte.keys():
            #print cte[tmp]
            rom+=cte[tmp]
        else:
            #print "not found:",tmp
            while tmp>0:
                for i in ctax:
                    #print "  matching with",i
                    if tmp/i>0:
                        #print "     match found:",tmp/i
                        rom+=cte[i]*(tmp/i)
                        #print rom
                        tmp%=i
                        #print tmp

        #print tmp
        num%=cta[len(str(num))-1]
        #raw_input()

    return rom

print solution(1),'I'
print solution(4),'IV'
print solution(6),'VI'
print solution(1321),'MCCCXXI'
print solution(1548),'MDXLVIII'
print solution(1984),'MCMLXXXIV'
