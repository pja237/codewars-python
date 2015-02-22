#!/usr/bin/python

cte={ 1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M' }
cta=[1,10,100,1000]
ctax=[1000,500,100,50,10,5,1]
ct={ 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }


class RomanHelper:
    def to_roman(self,num):
        rom=''
        while num>0:
            tmp=(num/cta[len(str(num))-1])*cta[len(str(num))-1]
            if tmp in cte.keys():
                rom+=cte[tmp]
            else:
                while tmp>0:
                    for i in ctax:
                        if tmp/i>0:
                            rom+=cte[i]*(tmp/i)
                            tmp%=i
            num%=cta[len(str(num))-1]
        return rom

        
    def from_roman(self,string):
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

RomanNumerals=RomanHelper()
print RomanNumerals.to_roman(1000)
print RomanNumerals.from_roman('M')
