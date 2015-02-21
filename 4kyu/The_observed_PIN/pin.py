#!/usr/bin/python


pins={ 1:(1,2,4), 2:(1,2,3,5), 3:(2,3,6), 4:(1,4,5,7), 5:(2,4,6,8,5), 6:(3,5,9,6), 7:(4,7,8), 8:(5,7,8,9,0), 9:(6,8,9), 0:(8,0) }

def expand_pins(input):
    expanded_set=[]
    for i in input:
        expanded_set.append(pins[int(i)])

    return expanded_set

allpins=set()

def recurse(pinset,way=''):
    global allpins

    if pinset==[]: 
        allpins.add(way)
        return 

    for i in pinset[0]:
        recurse(pinset[1:],way+str(i))

    return 

def get_pins(opin):
    epins=expand_pins(opin)
    recurse(epins)
    return epins

print get_pins('280')
print sorted(allpins)
